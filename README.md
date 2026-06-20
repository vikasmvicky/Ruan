# Ruan 🤖
### AI-Powered Business Intelligence for India's Small Vendors

> *"Every big company has a data team. Every small business has a rough book. Ruan closes that gap — in your language, in your city, for free."*

## 🚀 Live Demo
**Try Ruan now:** [ruan-vikasmvicky.streamlit.app](https://ruan-vikasmvicky.streamlit.app) *(update with your actual URL)*

---

## The Problem

India has **5.70 crore registered MSMEs** (Ministry of MSME, Udyam Portal, December 2024) contributing **35.4% of India's GDP** and employing **24.14 crore people**. Yet only **13% actively use any data analytics tools** (META Report Card 2025, indiasmeforum.org).

This is not unwillingness — it's lack of access. Every existing tool assumes:
- Clean structured CSV files
- English fluency
- ₹2,000+/month subscription budgets
- Technical literacy to read dashboards

India's digital literacy rate stands at just **37%** (NASSCOM). Most vendors track sales in handwritten registers, not spreadsheets — and the same profit number means a completely different thing depending on which city you're in.

**Ruan was built to fix this.**

---

## The Solution

Ruan is India's first **contextually intelligent AI business analyst** for small vendors — combining data analysis, regional language conversation, and economic context awareness in one free tool.

### 4-Layer Intelligence System

| Layer | What it does |
|-------|--------------|
| **1. Raw Data Analysis** | Pandas processes uploaded data — revenue, profit, margin, best/worst products |
| **2. Industry Benchmarking** | Compares margins against normal ranges for the vendor's specific business type |
| **3. Geographic Context** | City-specific cost database (25+ cities) — ₹20K profit in Mysuru ≠ Bangalore |
| **4. Seasonal Intelligence** | Understands India's business calendar — Diwali stock spikes aren't losses |

---

## Features

**Three ways to add data**
- 📁 Upload CSV / Excel
- 📷 Photo of handwritten register (OCR via Tesseract)
- 💬 Talk to Ruan — type or speak naturally, LLM extracts structured sales data

**AI Conversation**
- Groq Llama 3.3 70B-powered chat
- Kannada, Hindi, Tamil, English support
- Voice input via Groq Whisper transcription
- Simple vs Detailed response modes

**Memory**
- ChromaDB RAG vector memory — remembers analyses and conversations across sessions
- Sacred Timeline — visual history of business performance

**Visualizations**
- Revenue vs Profit vs Loss
- Daily profit trend (7-day rolling average)
- Product performance ranking
- Profit margin gauge vs industry benchmark
- Sales by day of week

**Privacy**
- Vendor data isolation — each vendor's history stored separately
- No data sharing between users
- Local-first architecture, no mandatory cloud dependency

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| LLM | Groq + Llama 3.3 70B |
| Orchestration | LangChain |
| Memory | ChromaDB + SentenceTransformers |
| Voice | Groq Whisper API |
| OCR | Tesseract |
| Analysis | Pandas + NumPy |
| Charts | Plotly |
| Offline Option | Ollama + Phi3 |

**Total cost to run: ₹0/month**

---

## Project Structure

```
ruan/
├── app.py
├── requirements.txt
├── core/
│   ├── analyst.py        # 4-layer intelligence engine
│   ├── llm.py             # Groq LLM + Ruan persona
│   ├── memory.py          # ChromaDB RAG memory
│   ├── charts.py          # Plotly visualizations
│   ├── data_entry.py      # OCR + conversational entry
│   └── voice.py           # Voice transcription
├── ui/
│   ├── ruan.py             # Ruan + Owly animations
│   └── theme.py            # Forest theme + widget
└── data/
    ├── vendors/            # Per-vendor isolated history
    └── memory_db/          # ChromaDB vector store
```

---

## Setup

```bash
git clone https://github.com/vikasmvicky/Ruan.git
cd Ruan
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key_here" > .env
streamlit run app.py
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

---

## Research Sources

| Statistic | Source |
|-----------|--------|
| 5.70 crore MSMEs registered | Ministry of MSME, Udyam Portal, Dec 2024 |
| 35.4% of India's GDP | META Report Card 2025, indiasmeforum.org |
| Only 13% use data analytics | META Report Card 2025 / NASSCOM-Deloitte MSME Digital Index |
| 37% digital literacy rate | NASSCOM, 2024 |

---

## Economic Impact

Ruan doesn't replace data analyst jobs — it serves the 63 million businesses that **never could afford one**. As these businesses grow through better decisions, they create new demand for human analysts. Better small-business decisions strengthen India's broader economy.

---


---

*Built for India's small businesses. 100% private. 100% free. Forever.*
