# 🤖 Ruan — AI Business Copilot for India's Small Businesses

*"Every big company has a data team. Every small business has a rough book. Ruan closes that gap — in your language, in your city, for free."*
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![AI](https://img.shields.io/badge/AI-Groq-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

---

## 🚀 Live Demo

🌐 **Try Ruan:** https://jesubmmguzkybaiwwnsgrb.streamlit.app/#ruan-top

💻 **GitHub Repository:** https://github.com/vikasmvicky/Ruan

---

## 🎯 The Problem

India has **5.70 crore registered MSMEs** contributing approximately **35.4% of India's GDP** and employing over **24 crore people**. Despite their economic importance, digital adoption remains limited, and many businesses still maintain records in notebooks, registers, and informal notes.

Most business analytics tools assume:

* Clean, structured spreadsheets
* English proficiency
* Paid subscriptions
* Technical knowledge to interpret dashboards

For millions of small businesses, these assumptions create a significant accessibility gap.

Ruan was built to bridge that gap.

---

## 💡 The Solution

**Ruan** is an AI-powered Business Intelligence Copilot designed specifically for India's MSMEs. It enables vendors to digitize business records and receive actionable insights through natural, familiar interactions.

Ruan combines:

* Business analytics
* Conversational AI
* OCR-based digitization
* Context-aware insights
* Multilingual interaction

All within one accessible platform.

---

## 🧠 Four-Layer Intelligence System

| Layer                 | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| Raw Data Analysis     | Revenue, profit, margins, product performance analysis      |
| Industry Benchmarking | Compare business performance with industry norms            |
| Geographic Context    | Interpret performance relative to local economic conditions |
| Seasonal Intelligence | Understand festivals and seasonal business patterns         |

---

## ✨ Features

### 📁 CSV & Excel Analysis

Upload business data and automatically generate:

* Revenue analysis
* Profit insights
* Product performance rankings
* Interactive dashboards

---

### 📷 Register Digitization (OCR)

Convert handwritten business registers into structured digital records using Tesseract OCR.

---

### 💬 Conversational Data Entry

Examples:

* "Today tea sales were ₹7000."
* "Coffee sales were ₹10000 and ingredients cost ₹3000."

Ruan extracts structured information automatically.

---

### 🎤 Voice Interaction

Speak naturally in:

* English
* Kannada
* Hindi
* Tamil

Speech is transcribed and converted into structured business information.

---

### 📊 Business Intelligence Dashboard

Generate:

* Revenue trends
* Profit and loss summaries
* Product performance insights
* Industry comparisons
* Visual analytics

---

## 🧠 Memory System

* ChromaDB vector memory
* Session-aware conversations
* Historical business insights
* Vendor-specific data isolation

---

## 🔒 Privacy

* Vendor data isolation
* No cross-user data sharing
* Local-first architecture
* No mandatory cloud dependency

---

## 🛠️ Tech Stack

| Layer          | Technology                      |
| -------------- | ------------------------------- |
| Frontend       | Streamlit                       |
| LLM            | Groq + Llama 3.3 70B            |
| Orchestration  | LangChain                       |
| Memory         | ChromaDB + SentenceTransformers |
| Voice          | Groq Whisper                    |
| OCR            | Tesseract OCR                   |
| Analytics      | Pandas + NumPy                  |
| Visualizations | Plotly                          |
| Offline Option | Ollama + Phi-3                  |

---

## 📂 Project Structure

```text
ruan/
├── app.py
├── requirements.txt
├── packages.txt
├── core/
│   ├── analyst.py
│   ├── llm.py
│   ├── memory.py
│   ├── charts.py
│   ├── data_entry.py
│   └── voice.py
├── ui/
│   ├── ruan.py
│   └── theme.py
└── data/
    ├── vendors/
    └── memory_db/
```

---

## ⚙️ Setup

```bash
git clone https://github.com/vikasmvicky/Ruan.git
cd Ruan

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

echo "GROQ_API_KEY=your_key_here" > .env

streamlit run app.py
```

---

## 📸 Screenshots

* Home Page
  <img width="1920" height="1080" alt="Screenshot (848)" src="https://github.com/user-attachments/assets/e1d31790-cd4f-49da-9af1-aca6554e1dc1" />

* Conversational Sales Entry
 <img width="1920" height="1080" alt="Screenshot (846)" src="https://github.com/user-attachments/assets/5e9ccaf1-eb9a-423c-83a2-e519e497b837" />
 *image of ruan and owly
 <img width="1920" height="1080" alt="Screenshot (922)" src="https://github.com/user-attachments/assets/1ff750e2-495b-4a09-aa77-efe5359a4a30" />


* Business Dashboard
  <img width="1920" height="1080" alt="Screenshot (923)" src="https://github.com/user-attachments/assets/e77a6c9d-d4fd-433b-97bb-ac76bd0aa74c" />



---

## 🌍 Vision

Ruan does not replace human analysts.

Instead, it empowers millions of businesses that have never had access to data analysis tools. By enabling better business decisions, Ruan contributes toward a more data-driven and digitally inclusive MSME ecosystem.

---

## 👨‍💻 Author

**Vikas M**
B.E. Computer Science and Engineering
Global Academy of Technology, Bengaluru

📧 [vikasgowdam022@gmail.com](mailto:vikasgowdam022@gmail.com)
💻 https://github.com/vikasmvicky
🔗 Add your LinkedIn URL

---

**Built for India's small businesses. Private. Accessible. Free.**
