# SemanticPDF-RAG

SemanticPDF-RAG is a Retrieval-Augmented Generation (RAG) project that enables semantic search and interactive querying over PDF documents. Upload your PDF files, generate vector embeddings, and then perform natural language queries to retrieve relevant information from the document using large language models (LLMs).

---

## Features

- Upload PDF documents for processing and chunking
- Generate and save vector embeddings from document chunks
- Perform semantic similarity search using user queries
- Integrate with an LLM to generate human-readable answers based on retrieved document context
- Streamlit-based interactive web app for ease of use

---

## Folder Structure

SemanticPDF-RAG/
│
├── data/ # Directory to store uploaded PDF files
├── embeddings/ # Directory where generated embeddings are saved
├── app.py # Streamlit app to run the UI and handle interactions
├── data_loader.py # Module to load and chunk PDF documents
├── embedding_generator.py # Module to generate embeddings for document chunks
├── llm_client.py # Module to query the LLM with retrieved context
└── query_embed.py # Module for generating embeddings for user queries

yaml
Copy
Edit

---

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/SemanticPDF-RAG.git
   cd SemanticPDF-RAG
Create and activate a Python virtual environment (recommended):

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your environment variables (e.g., API keys for LLM):

bash
Copy
Edit
export GOOGLE_API_KEY="your_api_key_here"  # Linux/macOS
set GOOGLE_API_KEY=your_api_key_here       # Windows
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
How to Use
Upload a PDF document via the web interface.

Click the button to convert the PDF into vector embeddings (chunks are created and saved).

Enter a natural language query related to the contents of the uploaded PDF.

Submit the query to retrieve semantically similar chunks.

The LLM will generate a concise, context-aware answer based on the retrieved content.

Notes
This project is framework-agnostic and can be extended with different vector databases or LLM providers.

Ensure your API keys and secrets are kept secure.

Currently, the app uses Streamlit for rapid prototyping and demo purposes.

Contribution
Contributions are welcome! Feel free to open issues or pull requests for bug fixes, new features, or improvements.
