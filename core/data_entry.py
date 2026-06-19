import pandas as pd
import pytesseract
from PIL import Image
import os
import re
import json
from datetime import datetime

# Set tesseract path for Windows
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    )


# ── OCR — Photo to text ────────────────────────────────────
def extract_text_from_image(image_file):
    """Extract text from uploaded photo of rough register"""
    try:
        image = Image.open(image_file)
        # Preprocess for better accuracy
        image = image.convert('L')  # grayscale
        text = pytesseract.image_to_string(image, lang='eng')
        return text.strip()
    except Exception as e:
        print(f"OCR error: {e}")
        return None


# ── Parse OCR text into structured rows ───────────────────
def parse_register_text(raw_text):
    """
    Convert messy OCR text into structured rows.
    Handles formats like:
    'Crocin 50 15' or 'Crocin - 50 units - Rs 15'
    """
    rows = []
    lines = raw_text.split('\n')

    for line in lines:
        line = line.strip()
        if not line or len(line) < 3:
            continue

        # Find numbers in the line
        numbers = re.findall(r'\d+\.?\d*', line)
        # Find text (product name) - remove numbers
        text_only = re.sub(r'\d+\.?\d*', '', line).strip()
        text_only = re.sub(r'[^\w\s]', '', text_only).strip()

        if text_only and len(numbers) >= 1:
            row = {
                "Item": text_only,
                "Quantity": float(numbers[0]) if len(numbers) > 0 else 0,
                "Price": float(numbers[1]) if len(numbers) > 1 else 0,
                "Date": datetime.now().strftime("%Y-%m-%d")
            }
            rows.append(row)

    return rows


def ocr_to_dataframe(image_file):
    """Complete pipeline: photo → dataframe"""
    raw_text = extract_text_from_image(image_file)
    if not raw_text:
        return None, "Could not read text from image"

    rows = parse_register_text(raw_text)
    if not rows:
        return None, "Could not find structured data in image"

    df = pd.DataFrame(rows)
    return df, raw_text


# ── Conversational data entry ──────────────────────────────
def extract_sale_from_text(text, llm_ask_function, vendor, business, city):
    """
    Use LLM to extract structured sale data from natural language.
    Example input: "Aaj maine 50 Crocin becha 15 rupaye mein"
    Returns: {"item": "Crocin", "quantity": 50, "price": 15}
    """
    prompt = f"""Extract sales information from this message.
Return ONLY valid JSON, nothing else.

Message: "{text}"

Format:
{{"item": "product name", "quantity": number, "price": number, "found": true}}

If no clear sale information is found, return:
{{"found": false}}

Examples:
"Aaj 50 Crocin becha 15 rupaye mein" 
→ {{"item": "Crocin", "quantity": 50, "price": 15, "found": true}}

"30 Dolo sold at 22 each"
→ {{"item": "Dolo", "quantity": 30, "price": 22, "found": true}}

"ಇಂದು 20 Vicks ಮಾರಾಟ ಮಾಡಿದೆ ₹40 ಗೆ"
→ {{"item": "Vicks", "quantity": 20, "price": 40, "found": true}}
"""

    try:
        from core.llm import get_client
        client = get_client()
        if not client:
            return None

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.1
        )

        result_text = response.choices[0].message.content.strip()
        # Clean up — remove markdown code blocks if present
        result_text = result_text.replace("```json", "").replace("```", "").strip()

        result = json.loads(result_text)
        return result

    except Exception as e:
        print(f"Extract sale error: {e}")
        return None


def save_conversational_entry(vendor_name, item, quantity, price):
    """Save a single sale entry built via conversation"""
    try:
        safe_name = vendor_name.replace(" ", "_").lower().strip()
        folder = f"data/vendors/{safe_name}"
        os.makedirs(folder, exist_ok=True)

        entries_path = f"{folder}/entries.json"

        # Load existing entries
        entries = []
        if os.path.exists(entries_path):
            with open(entries_path) as f:
                entries = json.load(f)

        # Add new entry
        entries.append({
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Item": item,
            "Quantity": quantity,
            "Price": price,
            "Sales": quantity * price
        })

        # Save back
        with open(entries_path, "w") as f:
            json.dump(entries, f, indent=2)

        return True
    except Exception as e:
        print(f"Save entry error: {e}")
        return False


def get_vendor_entries_as_df(vendor_name):
    """Load all conversational entries as a dataframe"""
    try:
        safe_name = vendor_name.replace(" ", "_").lower().strip()
        entries_path = f"data/vendors/{safe_name}/entries.json"

        if not os.path.exists(entries_path):
            return None

        with open(entries_path) as f:
            entries = json.load(f)

        if not entries:
            return None

        return pd.DataFrame(entries)
    except Exception as e:
        print(f"Load entries error: {e}")
        return None


def export_entries_to_excel(vendor_name):
    """Export vendor's conversational entries to downloadable Excel"""
    df = get_vendor_entries_as_df(vendor_name)
    if df is None:
        return None

    safe_name = vendor_name.replace(" ", "_").lower().strip()
    folder = f"data/vendors/{safe_name}"
    excel_path = f"{folder}/sales_data.xlsx"

    df.to_excel(excel_path, index=False, engine='openpyxl')
    return excel_path