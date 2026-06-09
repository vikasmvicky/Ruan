# Ruan 🤖

## AI-Powered Business Intelligence for Small Businesses

> *Helping small businesses understand their data, improve profitability, and make better decisions through AI-powered business analytics.*

---

## Overview

Ruan is an AI-powered business intelligence platform designed for small businesses and local vendors. It transforms sales data into actionable insights through automated analysis, interactive visualizations, contextual business recommendations, and natural language conversations.

Unlike traditional analytics tools that require technical expertise, Ruan allows business owners to upload their sales data and receive easy-to-understand insights about revenue, profit, product performance, customer trends, and business health.

The platform combines data analytics, business benchmarking, city-aware recommendations, multilingual AI assistance, and long-term memory to create a personalized business advisor experience.

---

## Key Features

### Business Analytics Engine

* Revenue and profit analysis
* Profit margin calculation
* Average order value tracking
* Loss-making order detection
* Product profitability analysis
* Segment performance analysis
* City-wise business performance insights
* Monthly and daily trend analysis
* Discount impact analysis
* Freight cost optimization insights

### AI-Powered Business Assistant

* Conversational business advisor powered by Llama 3.3 70B
* Natural language business queries
* Context-aware recommendations
* Vendor-specific responses
* Personalized business guidance
* Historical business memory integration

### Multilingual Support

Supports:

* English
* Kannada
* Hindi
* Tamil

Business owners can interact with Ruan in their preferred language and receive responses accordingly.

### Smart Business Intelligence

Ruan combines multiple intelligence layers:

#### Industry Benchmarking

Business-specific benchmark ranges for:

* Medical Shops
* Kirana Stores
* Textile Shops
* Shoe Showrooms
* Fancy Stores
* Vegetable Vendors
* Pan Shops
* Hardware Stores

#### City-Aware Analysis

Ruan understands business context across different Indian cities by considering:

* Cost of living
* Rental expectations
* Minimum viable profit targets
* Local business conditions

### Interactive Visualizations

* Revenue vs Profit vs Loss analysis
* Daily profit trend tracking
* Rolling average performance trends
* Product profitability rankings
* Profit margin benchmark gauges
* Day-of-week performance analysis

### Memory & Personalization

Ruan remembers previous business analyses using vector-based memory.

Features include:

* Vendor-specific memory
* Analysis history tracking
* Semantic memory retrieval
* Context-aware conversations
* Long-term business insights

### Smart Data Detection

* Automatic dataset recognition
* Sales data validation
* Partial dataset support
* Best-effort analysis for unconventional formats
* Graceful fallback recommendations

---

## Technology Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### AI & Language Models

* Groq API
* Llama 3.3 70B Versatile

### Vector Memory

* ChromaDB
* Sentence Transformers
* all-MiniLM-L6-v2 Embedding Model

### Storage

* JSON-based persistence
* Local vendor data storage
* Persistent vector database

---

## System Architecture

```text
User
 │
 ▼
Streamlit Interface
 │
 ▼
Business Profile Setup
 │
 ▼
Data Upload
 │
 ▼
Smart Data Detection
 │
 ▼
Analytics Engine
 │
 ├── Revenue Analysis
 │
 ├── Profit Analysis
 │
 ├── Product Analysis
 │
 ├── Benchmark Analysis
 │
 └── City Context Analysis
 │
 ▼
Visualization Layer
 │
 ▼
RAG Memory System
 │
 ▼
Groq Llama 3.3 70B
 │
 ▼
Business Recommendations
```

---

## Project Structure

```text
ruan/
│
├── app.py
├── requirements.txt
├── README.md
│
├── core/
│   ├── analyst.py
│   ├── charts.py
│   ├── llm.py
│   └── memory.py
│
├── ui/
│   ├── ruan.py
│   └── theme.py
│
├── data/
│   ├── vendors/
│   └── memory_db/
│
└── .env
```

---

## How It Works

### Step 1

Create a business profile by entering:

* Name
* City
* Business type
* Preferred language

### Step 2

Upload sales data in:

* CSV format
* Excel format

### Step 3

Ruan automatically:

* Detects the dataset structure
* Extracts business insights
* Calculates key metrics
* Generates visualizations

### Step 4

Chat with Ruan and ask questions such as:

* Why is my profit low?
* Which product earns the most profit?
* Which day performs best?
* Are discounts hurting my business?
* What should I improve next month?

### Step 5

Receive personalized recommendations based on:

* Current business performance
* Historical analyses
* Industry benchmarks
* City-specific context

---

## Privacy

Ruan is designed with privacy in mind.

* Vendor data remains local
* Business history is stored separately
* Memory retrieval is vendor-specific
* No business data is shared between vendors

---

## Future Enhancements

Currently under development:

* OCR-based register book reading
* Handwritten sales record extraction
* Voice-based business interaction
* Speech-to-analysis workflow
* WhatsApp sales report parsing
* Mobile application
* Inventory management module
* Business forecasting models
* Additional Indian language support

---

## Vision

Small businesses generate enormous amounts of data but rarely have access to professional analytics tools.

Ruan aims to bridge this gap by providing an intelligent, multilingual, and accessible business advisor that helps business owners understand their numbers and make better decisions without requiring technical expertise.

---

## License

MIT License

Feel free to use, modify, and contribute to the project.

