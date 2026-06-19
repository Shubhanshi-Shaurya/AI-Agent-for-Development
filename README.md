#  Multi-Agent AI App Builder

An interactive web application built with Streamlit that leverages a multi-agent AI pipeline to plan, develop, test, and review application code. Powered by local LLMs via Ollama, this project demonstrates how specialized AI agents can collaborate sequentially to automate full-stack software development workflows.

---

##  Features

* **Interactive Streamlit UI:** A clean frontend interface with dynamic status indicators to monitor agent workflows in real-time.
* **Sequential Agent Collaboration:** 
  1. **Planner Agent:** Breaks down the prompt and designs the application logic.
  2. **Developer Agent:** Converts the blueprint into clean, structured Python code.
  3. **Tester Agent:** Validates logic, runs simulated edge cases, and writes test coverage reports.
  4. **Reviewer Agent:** Inspects code for readability, performance, and best practices.
* **100% Local & Private:** Runs entirely on your local machine using Ollama—no API keys or internet connection required.

---

##  Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM Framework:** [LangChain / LangChain-Ollama](https://github.com/langchain-ai/langchain)
* **Local Inference:** [Ollama](https://ollama.com/) (Using models like `llama3` or `llama3.2:1b`)
* **Language:** Python 3.10+

---

##  Installation & Setup

Follow these steps to set up and run the project locally on your machine.

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed and running on your system. 

Download your preferred lightweight model via your terminal:
```bash
ollama run llama3.2:1b

```

### 2. Clone the Repository
```bash

git clone [https://github.com/Shubhanshi-Shaurya/AI-Agent-for-Development](https://github.com/Shubhanshi-Shaurya/AI-Agent-for-Development)
cd AI-Agent-for-Development

cd AI-Agent-for-Development

```

### 3. Set Up Virtual Environment
Create and activate a isolated Python virtual environment:

```bash

# Windows
python -m venv .venv
.venv\Scripts\activate

```

### 4. Install Dependencies

```bash

pip install streamlit langchain-ollama

```

### 5.Usage
1. Make sure your local Ollama instance is active.
2. Launch the Streamlit web application:

```bash

streamlit run app.py

```

3. Open your browser and navigate to http://localhost:8501.

4. Enter an application idea and click Generate App to watch the agents collaborate!

## Project Structure
```text

ai_agent
    ├── .venv
    ├── .gitignore 
    ├── requirements.txt         
    ├── app.py              
    └── README.md   

```        