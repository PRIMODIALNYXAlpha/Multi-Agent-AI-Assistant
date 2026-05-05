# 🤖 Multi-Agent AI Assistant (LangGraph + Groq + Tavily)

## 📌 Overview

This project is an **Enterprise-level Multi-Agent AI System** where multiple AI agents collaborate to solve complex tasks such as research, coding, and debugging.

Built using **LangGraph**, this system simulates a team of AI agents working together in a structured workflow.

---

## 🚀 Features

* 🧠 Multi-agent collaboration system
* 🔗 LangGraph workflow orchestration
* 🔍 Real-time web search using Tavily API
* 💻 Code generation using Groq LLM
* 🐞 Automatic debugging and fixing
* ⚡ Fast responses with Groq
* 🌐 Interactive UI with Streamlit

---

## 🧠 System Workflow

```text
User Input
   ↓
Task Agent (Planner)
   ↓
Research Agent (Tavily)
   ↓
Software Agent (Code Generator)
   ↓
Debug Agent (Fixes Code)
   ↓
Final Output
```

---

## 📁 Project Structure

```text
multi-agent-ai-assistant/
│
├── app/
│   ├── agents/
│   │   ├── task_agent.py
│   │   ├── research_agent.py
│   │   ├── software_agent.py
│   │   └── debug_agent.py
│   ├── graph/
│   ├── memory/
│   ├── tools/
│   ├── config.py
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── .env (not included in repo)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/PRIMODIALNYXAlpha/Multi-Agent-AI-Assistant.git
cd multi-agent-ai-assistant-main
```

---

### 2. Create virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Keys

Create `.env` file:

```text
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

---

### 5. Run the project

```bash
python -m streamlit run streamlit_app.py
```

---

## 🎯 Usage

Enter complex tasks like:

* "Build a Flask login system"
* "Create a REST API with authentication"
* "Explain RAG and implement it in Python"

---

## 🧠 Technologies Used

* Python
* Streamlit
* LangGraph
* Groq API
* Tavily API

---

## ⚠️ Notes

* `.env` is excluded for security
* Requires internet for API calls
* Use Python 3.11 for best compatibility

---

## 🚀 Future Improvements

* Chat memory integration
* Deployment (Streamlit Cloud / AWS)
* UI enhancements
* Multi-user support

---

## 👨‍💻 Author

**Tarun SR**

---

## ⭐ Conclusion

This project demonstrates how modern AI systems use multiple agents, tools, and workflows to solve real-world problems efficiently.

⭐ If you like this project, consider starring the repo!
