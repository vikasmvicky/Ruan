import os
from groq import Groq

_memory_store = {}


def get_api_key():
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
    try:
        env_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), '.env'
        )
        with open(env_path) as f:
            for line in f:
                if line.startswith('GROQ_API_KEY='):
                    return line.strip().split('=', 1)[1]
    except Exception as e:
        print(f"API key error: {e}")
    return None


def get_client():
    key = get_api_key()
    if not key:
        return None
    return Groq(api_key=key)


def get_vendor_memory(vendor_name):
    if vendor_name not in _memory_store:
        _memory_store[vendor_name] = []
    return _memory_store[vendor_name]


def ask_ruan(
    question, vendor, business,
    city, language, insights,
    response_style="detailed"
):
    try:
        client = get_client()
        if not client:
            return "API key not found! Check your .env file. 🤖"

        if insights:
            insight_str = (
                f"Revenue: Rs {insights.get('total_revenue',0):,.0f}\n"
                f"Profit: Rs {insights.get('total_profit',0):,.0f}\n"
                f"Margin: {insights.get('profit_margin',0)}%\n"
                f"Best product: {insights.get('best_product','N/A')}\n"
                f"Worst product: {insights.get('worst_product','N/A')}\n"
                f"Best day: {insights.get('best_day','N/A')}\n"
                f"Worst day: {insights.get('worst_day','N/A')}\n"
                f"Loss orders: {insights.get('loss_orders',0)}\n"
                f"Total orders: {insights.get('total_orders',0)}"
            )
        else:
            insight_str = "No data uploaded yet"

        # Try to get RAG memories
        memory_context = ""
        try:
            from core.memory import get_relevant_memories
            memories = get_relevant_memories(vendor, question, n=3)
            if memories:
                memory_context = (
                    "\n\nRelevant past information:\n" +
                    "\n---\n".join(memories[:3])
                )
        except Exception:
            pass

        if response_style == "simple":
            style_instruction = """
RESPONSE STYLE: SIMPLE MODE
- Maximum 2 lines only
- Line 1: What is the problem in ONE simple sentence
- Line 2: Exactly what to do TODAY in ONE sentence
- No explanations. No reasoning. Just action.
"""
        else:
            style_instruction = """
RESPONSE STYLE: DETAILED MODE
- Friendly conversational tone
- Answer ALL questions the vendor asks
- If multiple questions — answer each one clearly
- Give specific numbers from the data
- End with ONE clear action to take today
- Maximum 200 words total
- Use emojis naturally
"""

        if language == "Kannada":
            language_instruction = """
CRITICAL: Respond ONLY in Kannada script.
Use simple everyday Kannada words.
Write with correct Kannada spelling.
Only keep product names in English.
Common words:
- ನಿಮ್ಮ = your, ಅಂಗಡಿ = shop
- ಲಾಭ = profit, ನಷ್ಟ = loss
- ಮಾರಾಟ = sales, ಇಂದು = today
"""
        elif language == "Hindi":
            language_instruction = """
CRITICAL: Respond ONLY in Hindi (Devanagari) script.
Use simple everyday Hindi words.
Write with correct Hindi spelling.
Only keep product names in English.
Common words:
- आपकी = your, दुकान = shop
- लाभ = profit, नुकसान = loss
- बिक्री = sales, आज = today
"""
        elif language == "Tamil":
            language_instruction = """
CRITICAL: Respond ONLY in Tamil script.
Use simple everyday Tamil words.
Write with correct Tamil spelling.
Only keep product names in English.
"""
        else:
            language_instruction = "LANGUAGE: Respond in clear simple English."

        history = get_vendor_memory(vendor)

        system_prompt = f"""You are Ruan, a friendly and energetic AI
business assistant for small vendors in India.
You are like a helpful genius who loves data
and wants to help small shop owners succeed.

Your personality:
- Always warm, friendly, encouraging
- Never use technical jargon
- You know Indian business context deeply
- Each city has its own economic parameters —
  rent, cost of living, competition density,
  purchasing power — all different per city.
  True business intelligence must be location-aware.
- You care genuinely about the vendor success
- Always address vendor by name: {vendor}

Business context:
- Vendor: {vendor}
- Business: {business}
- City: {city}
- Language: {language}

Current data:
{insight_str}
{memory_context}

{style_instruction}
{language_instruction}"""

        messages = [{"role": "system", "content": system_prompt}]

        for msg in history[-6:]:
            messages.append(msg)

        messages.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=800,
            temperature=0.7
        )

        answer = response.choices[0].message.content.strip()

        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})

        return answer

    except Exception as e:
        print(f"Ruan LLM error: {e}")
        return f"Something went wrong! Please try again. Error: {str(e)[:60]}"


def test_llm_connection():
    try:
        client = get_client()
        if not client:
            return False, "API key not found"
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say hello in one word"}],
            max_tokens=10
        )
        return True, response.choices[0].message.content
    except Exception as e:
        return False, str(e)