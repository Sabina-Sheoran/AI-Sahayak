<div align="center">

# 🌾 AI Sahayak (SabbiAI)
### *AI-Powered Livelihood Assistant for Rural India*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=for-the-badge)](https://github.com/Sabina-Sheoran)

---

> **AI Sahayak** is a multilingual, voice-enabled AI assistant designed to help rural Indian citizens discover and apply for government welfare schemes, job opportunities, and livelihood support — in their own language.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Application Flowchart](#-application-flowchart)
- [Data Flow Diagram](#-data-flow-diagram)
- [Module Structure](#-module-structure)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Future Roadmap](#-future-roadmap)
- [Credits](#-credits)

---

## 🌟 Overview

Rural India faces a massive **information gap** — millions of eligible citizens miss out on government welfare schemes simply because they don't know about them or can't navigate complex forms. **AI Sahayak** bridges this gap by:

- 🗣️ **Speaking the local language** — multilingual voice input/output (Hindi, English, and regional dialects)
- 🤖 **Explaining government schemes** in plain, simple terms via an AI agent
- 📋 **Checking eligibility** automatically based on user profile
- 🔍 **Recommending schemes** tailored to the user's location, income, occupation, and family situation
- 📢 **Reading aloud** — accessible even for low-literacy users via Text-to-Speech

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎙️ **Voice Input** | Speak your query in Hindi/English via microphone |
| 🔊 **Text-to-Speech** | Responses read aloud using Microsoft Edge TTS |
| 🤖 **AI Agent** | Groq-powered LLM that understands context and follows up |
| 📚 **Schemes Database** | 20+ Indian government schemes (MGNREGA, PM-Kisan, etc.) |
| 🏷️ **NLP Classifier** | Keyword-based intent classification for scheme matching |
| 🧠 **AutoML Eligibility** | ML model to predict eligibility based on user profile |
| 🌐 **Web UI** | Clean HTML/CSS frontend with multiple pages |
| 📡 **REST API** | FastAPI backend with full API documentation |
| 💬 **Conversation History** | Maintains context across multiple turns |

---

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph Frontend["🌐 Frontend (HTML/CSS/JS)"]
        HOME[Home Screen]
        CHAT[Chat Interface]
        ELIG[Eligibility Form]
        SCHEME[Scheme Recommendations]
        ABOUT[About Page]
        SUPPORT[Support Page]
    end

    subgraph Backend["⚙️ FastAPI Backend (app.py)"]
        API[REST API Router]
        AGENT[AI Agent]
        NLP[NLP Classifier]
        AUTOML[AutoML Model]
        SPEECH[Speech API]
        DB[Schemes Database]
    end

    subgraph AI["🤖 AI / ML Layer"]
        GROQ[Groq LLM\nLlama 3.1]
        TTS[Microsoft Edge TTS]
        STT[SpeechRecognition]
        SKLEARN[Scikit-learn\nEligibility Model]
        TFIDF[TF-IDF Vectorizer]
    end

    HOME --> API
    CHAT --> API
    ELIG --> API
    SCHEME --> API

    API --> AGENT
    API --> NLP
    API --> AUTOML
    API --> SPEECH

    AGENT --> GROQ
    AGENT --> DB
    NLP --> TFIDF
    AUTOML --> SKLEARN
    SPEECH --> TTS
    SPEECH --> STT
```

---

## 🔄 Application Flowchart

```mermaid
flowchart TD
    A([👤 User Opens App]) --> B[Home Screen]
    B --> C{Choose Input Method}

    C -->|Text| D[Type Query in Chat]
    C -->|Voice| E[🎙️ Record Audio]

    E --> F[Speech-to-Text\nConversion]
    F --> D

    D --> G[Send to FastAPI Backend]

    G --> H{Intent Classification\nNLP Module}

    H -->|Scheme Query| I[Search Schemes Database]
    H -->|Eligibility Check| J[Run AutoML Model]
    H -->|General Query| K[Groq LLM Agent]
    H -->|Job/Livelihood| L[Livelihood Recommendations]

    I --> M[Filter Relevant Schemes]
    J --> N[Check User Profile\nIncome / Age / Category]
    K --> O[LLM Generates Response]
    L --> P[Match Job Schemes]

    M --> Q[Merge & Rank Results]
    N --> Q
    O --> Q
    P --> Q

    Q --> R[Format Response]
    R --> S{TTS Enabled?}

    S -->|Yes| T[🔊 Microsoft Edge TTS\nRead Aloud]
    S -->|No| U[📝 Display Text Response]

    T --> V[User Receives Answer]
    U --> V

    V --> W{Continue?}
    W -->|Yes - Follow-up| D
    W -->|No| X([✅ Session Ends])

    style A fill:#4CAF50,color:#fff
    style X fill:#4CAF50,color:#fff
    style GROQ fill:#FF9800,color:#fff
    style H fill:#2196F3,color:#fff
```

---

## 📊 Data Flow Diagram

```mermaid
sequenceDiagram
    actor User
    participant UI as 🌐 Frontend
    participant API as ⚙️ FastAPI
    participant Agent as 🤖 AI Agent
    participant NLP as 🔍 NLP Classifier
    participant DB as 📚 Schemes DB
    participant LLM as 🧠 Groq LLM
    participant TTS as 🔊 Edge TTS

    User->>UI: Speaks / Types query
    UI->>API: POST /api/chat {query, history}

    API->>NLP: classify_intent(query)
    NLP-->>API: intent + keywords

    API->>Agent: process_query(query, intent, history)
    Agent->>DB: search_schemes(keywords)
    DB-->>Agent: matching_schemes[]

    Agent->>LLM: generate_response(context + schemes)
    LLM-->>Agent: natural_language_response

    Agent-->>API: formatted_response

    API->>TTS: synthesize(response, language="hi")
    TTS-->>API: audio_file.mp3

    API-->>UI: {text: response, audio_url: /audio}
    UI-->>User: Display text + Play audio
```

---

## 📁 Module Structure

```
AI Sahayak/
│
├── 📄 app.py                     # FastAPI entry point & API routes
├── 📄 setup_datasets.py          # Dataset preparation & model training
├── 📄 requirements.txt           # Python dependencies
├── 📄 .env.example               # Environment variable template
│
├── 🗂️ backend/
│   ├── agent.py                  # AI Agent — Groq LLM integration & conversation
│   ├── schemes_db.py             # Government schemes knowledge base (20+ schemes)
│   ├── nlp_classifier.py         # Intent detection via TF-IDF + keywords
│   ├── automl_model.py           # ML eligibility predictor (scikit-learn)
│   ├── speech_api.py             # TTS (Edge TTS) + STT (SpeechRecognition)
│   └── __init__.py
│
├── 🗂️ UI/
│   ├── ai_sahayak_home_screen/   # Landing page
│   ├── gramin_clarity/           # Chat interface (main interaction)
│   ├── check_eligibility_form/   # Eligibility form & results
│   ├── scheme_recommendations/   # Filtered scheme cards
│   ├── about/                    # About the project
│   ├── support/                  # Contact & help
│   ├── assets/                   # Images, icons
│   └── styles/                   # Shared CSS
│
├── 🗂️ models/                    # Trained ML model files (.pkl)
├── 🗂️ data/                      # Datasets for training
└── 🗂️ temp_audio/                # Temporary TTS audio files
```

---

## 🛠️ Tech Stack

```mermaid
mindmap
  root((AI Sahayak))
    Frontend
      HTML5
      CSS3
      Vanilla JavaScript
    Backend
      FastAPI
      Uvicorn
      Python 3.10+
    AI & ML
      Groq API
        Llama 3.1 70B
      Scikit-learn
        TF-IDF Vectorizer
        Eligibility Classifier
      Microsoft Edge TTS
      SpeechRecognition
    Data
      Pandas
      NumPy
      Government Schemes DB
    Dev Tools
      python-dotenv
      Requests
      Plotly
```

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | HTML5 / CSS3 / JS | Multi-page web UI |
| **Backend** | FastAPI + Uvicorn | REST API server |
| **AI Agent** | Groq (Llama 3.1) | Natural language Q&A |
| **NLP** | TF-IDF + Keywords | Intent classification |
| **ML Model** | Scikit-learn | Eligibility prediction |
| **TTS** | Microsoft Edge TTS | Text-to-speech output |
| **STT** | SpeechRecognition | Voice input processing |
| **Data** | Pandas + NumPy | Data processing |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- A [Groq API key](https://console.groq.com/) (free tier available)

### 1. Clone the Repository

```bash
git clone https://github.com/Sabina-Sheoran/AI-Sahayak.git
cd AI-Sahayak
```

### 2. Create & Activate Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application

```bash
python app.py
```

The server starts at:
- 🌐 **App**: http://localhost:8000
- 📚 **API Docs**: http://localhost:8000/docs
- 🔄 **ReDoc**: http://localhost:8000/redoc

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serve the home page |
| `POST` | `/api/chat` | Send a query to the AI agent |
| `POST` | `/api/speech-to-text` | Convert audio to text |
| `POST` | `/api/text-to-speech` | Convert text to audio |
| `POST` | `/api/check-eligibility` | Check scheme eligibility |
| `GET` | `/api/schemes` | Get all government schemes |
| `GET` | `/api/schemes/search` | Search schemes by keyword |
| `GET` | `/docs` | Interactive Swagger API docs |

### Example API Request

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "मुझे MGNREGA के बारे में बताओ",
    "language": "hi",
    "conversation_history": []
  }'
```

### Example Response

```json
{
  "response": "MGNREGA (महात्मा गांधी राष्ट्रीय ग्रामीण रोजगार गारंटी अधिनियम) एक सरकारी योजना है जो...",
  "schemes_mentioned": ["MGNREGA"],
  "audio_url": "/temp_audio/response_123.mp3",
  "language": "hi"
}
```

---

## 🗃️ Government Schemes Covered

```mermaid
graph LR
    subgraph Employment["💼 Employment"]
        A[MGNREGA]
        B[PM Rojgar Protsahan]
        C[Mudra Yojana]
    end

    subgraph Agriculture["🌾 Agriculture"]
        D[PM-Kisan]
        E[Kisan Credit Card]
        F[PMFBY Insurance]
    end

    subgraph Housing["🏠 Housing"]
        G[PM Awas Yojana]
        H[Rural Housing Scheme]
    end

    subgraph Social["🛡️ Social Security"]
        I[PM Jan Dhan]
        J[Atal Pension Yojana]
        K[PM Jeevan Jyoti]
        L[Ujjwala Yojana]
    end

    subgraph Health["🏥 Health"]
        M[Ayushman Bharat]
        N[Janani Suraksha]
    end
```

---

## 🔮 Future Roadmap

- [ ] 🌍 **More Languages** — Support for 10+ regional languages (Tamil, Telugu, Bengali, etc.)
- [ ] 📱 **Mobile App** — Android app for offline-first usage in low-connectivity areas
- [ ] 🗺️ **Location-aware** — Recommend state-specific schemes based on GPS
- [ ] 📝 **Form Auto-fill** — Help users fill and submit applications automatically
- [ ] 🔔 **Alerts** — Notify users about new schemes or application deadlines
- [ ] 🤝 **Panchayat Integration** — Embed the assistant in local government portals
- [ ] 📊 **Analytics Dashboard** — Track which schemes are most queried in each region

---

## 🤝 Credits

<div align="center">

| | |
|---|---|
| 👩‍💻 **Developer** | [Sabina Sheoran](https://github.com/Sabina-Sheoran) |
| 🤖 **LLM Provider** | [Groq](https://groq.com) — Free AI API |
| 🔊 **TTS Engine** | Microsoft Edge TTS |
| 🎓 **Purpose** | Academic project for rural AI accessibility |

</div>

---

<div align="center">

**Made with ❤️ for Rural India**

*"Technology should serve everyone — not just those who can read it."*

⭐ Star this repo if you find it useful!

</div>