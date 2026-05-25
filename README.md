# 🤖 Enhanced Q&A Chatbot with Ollama

A simple AI-powered Q&A chatbot built using **Streamlit**, **LangChain**, and **Ollama**.

This project demonstrates how to create a chatbot interface using local Large Language Models (LLMs) without relying on paid APIs.

---

# 🚀 Features

✅ Interactive chatbot UI using Streamlit  
✅ Local LLM integration with Ollama  
✅ Prompt engineering using LangChain  
✅ Adjustable temperature and max token settings  
✅ LangSmith tracing support  
✅ Beginner-friendly project structure  

---

# 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- LangSmith
- Dotenv

---

# 📂 Project Structure

```bash
📦 enhanced-qa-chatbot
 ┣ 📜 app.py
 ┣ 📜 .env
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vinay-Rai/q-a-chatbot-with-ollama

cd q-a-chatbot-with-ollama
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Install Ollama

Download Ollama from the official website:

https://ollama.com/

---

# 📦 Pull the Model

```bash
ollama pull gemma:2b
```

You can also use other Ollama-supported models.

---

# 🔑 Setup Environment Variables

Create a `.env` file:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧠 How the Project Works (Easy Explanation)

This chatbot follows a simple AI workflow:

## Step 1: User Enters a Question

The user types a question into the Streamlit interface.

Example:

```text
What is Machine Learning?
```

---

## Step 2: Prompt Template is Created

LangChain creates a structured prompt using:

```python
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant"),
        ("user","Question:{question}")
    ]
)
```

The system message tells the AI how to behave.

The user question gets inserted dynamically.

---

## Step 3: Ollama Loads the Local LLM

```python
llm = Ollama(model="gemma:2b")
```

Ollama runs the model locally on your computer.

This means:
- No paid API required
- Faster local experimentation
- Better privacy

---

## Step 4: LangChain Creates the Chain

```python
chain = prompt | llm | output_parser
```

This creates a pipeline:

```text
User Question
   ↓
Prompt Template
   ↓
LLM (Ollama)
   ↓
Output Parser
   ↓
Final Response
```

---

## Step 5: AI Generates the Response

The chain processes the question and returns the answer.

```python
answer = chain.invoke({"question":question})
```

---

## Step 6: Response is Displayed

Streamlit displays the AI response on the web app interface.

---

# 🔄 Complete Project Flow

```text
User Input
    ↓
Streamlit UI
    ↓
Prompt Template
    ↓
LangChain Chain
    ↓
Ollama LLM
    ↓
Response Parsing
    ↓
Display Final Answer
```

---

# 📸 Application Preview

## Main Interface

- Select Model
- Adjust Temperature
- Set Max Tokens
- Ask Questions
- Get AI Responses

---

# 📈 Future Improvements

- Add conversation memory
- Support multiple Ollama models
- Add chat history
- Integrate vector databases
- Add RAG pipeline
- Voice input support
- Deploy on cloud

---

# 🎯 Learning Outcomes

By building this project, you will understand:

- How LLM applications work
- LangChain basics
- Prompt engineering
- LLM pipelines
- Local AI model execution
- Streamlit UI development

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository and improve the project.

---

# ⭐ Support

If you found this project helpful, give it a ⭐ on GitHub!

---

# 📬 Connect With Me

LinkedIn: www.linkedin.com/in/vinay-rai-24vr 

GitHub: https://github.com/Vinay-Rai