

# 🌐 Real-Time AI Assistant (Web RAG)

A **real-time Retrieval-Augmented Generation (RAG)** AI assistant that answers questions using **live web search**, powered by a **local LLM (Llama 3)** running via **Ollama**.  
No paid APIs. Fully open-source. Dockerized.

---

## 🚀 What This Project Does

- Takes a user question
- Searches the web **in real time** (DuckDuckGo)
- Injects search results as context
- Generates an answer using a **local LLM**
- Runs entirely on your machine

This avoids LLM knowledge cutoffs and provides **up-to-date answers**.

---

## 🧠 Architecture Overview



User
↓
Python Assistant (LangChain)
↓
DuckDuckGo Search ──┐
├─ Context → LLM (Llama 3 via Ollama)
Ollama Server ──────┘



---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Ollama** (local LLM runtime)
- **Llama 3 (8B)**
- **DuckDuckGo Search**
- **Docker & Docker Compose**

---

## 📁 Project Structure



genai-realtime-web-rag/
│
├── assistant.py          # Main RAG application
├── Dockerfile            # Docker build instructions
├── docker-compose.yml    # Multi-service orchestration
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore





## ⚙️ Setup Instructions (Local, Without Docker)

### 1️⃣ Install Ollama
Download and install from:
👉 https://ollama.com

Pull the model:

ollama pull llama3:8b

---

### 2️⃣ Create Python Environment


python -m venv venv
venv\Scripts\activate   # Windows


Install dependencies:


pip install -r requirements.txt


---

### 3️⃣ Run the Assistant


python assistant.py


---

## 🐳 Run Using Docker (Recommended)

### 1️⃣ Build & Run Everything


docker compose up --build


This will:

* Start Ollama
* Start the RAG assistant
* Connect them automatically

---

### 2️⃣ Example Interaction


🌐 Real-Time AI Assistant (Web RAG)
Type 'exit' to quit

You: What are today's trending AI topics?
🤖 Thinking...
🤖: Recent trends include multimodal AI models, open-source LLMs, and AI regulation discussions.


---

## 🧪 Why Docker Compose?

* One command starts **all services**
* Persistent model storage
* Production-style architecture
* Easy to deploy anywhere

---

## ⚠️ Limitations

* Web search quality depends on DuckDuckGo
* Large models require sufficient RAM
* Internet required for live search

---

## 🔮 Possible Extensions

* Streamlit web UI
* PDF + Web hybrid RAG
* Multi-agent search
* Cloud deployment (EC2 / Fly.io)

---

## 📌 Key Learning Outcomes

* Built a real-time RAG system
* Used local LLMs without paid APIs
* Applied LangChain LCEL
* Dockerized a GenAI application
* Orchestrated services with Docker Compose

---
