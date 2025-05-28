# SemanticPDF-RAG

**SemanticPDF-RAG** is a Retrieval-Augmented Generation (RAG) application that allows semantic search and question-answering over PDF documents using large language models (LLMs). Simply upload a PDF, generate embeddings, and ask questions in natural language to retrieve contextually accurate information from the document.

---

## 🚀 Features

- 📄 Upload any PDF document for semantic indexing
- 🔍 Generate vector embeddings of document chunks
- 🤖 Query the document with natural language questions
- 🧠 LLM generates answers from semantically similar document sections
- 🧪 Clean Streamlit interface for interactive use

---

## 🗂️ Folder Structure

SemanticPDF-RAG/
│
├── data/ # Directory to store uploaded PDF files
├── embeddings/ # Directory where generated embeddings are saved
├── app.py # Streamlit app to run the UI and handle user interaction
├── data_loader.py # Handles PDF reading, text extraction, and chunking
├── embedding_generator.py # Generates and stores document embeddings
├── llm_client.py # Sends similar chunks to LLM and returns answers
└── query_embed.py # Generates query embeddings for similarity search


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/SemanticPDF-RAG.git
cd SemanticPDF-RAG
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # For macOS/Linux
.venv\Scripts\activate         # For Windows
``` 
3. Install the required packages
``` bash
pip install -r requirements.txt
```
4. Set your environment variable
```bash
Copy
Edit
# Linux/macOS
export GOOGLE_API_KEY="your_google_api_key"

# Windows (Command Prompt)
set GOOGLE_API_KEY=your_google_api_key
