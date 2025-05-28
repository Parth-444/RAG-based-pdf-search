import streamlit as st
from data_loader import DocumentLoader
from embedding_generator import EmbeddingGenerator
from llm_client import LLMClient
import os
import tempfile

# Get current directory (where script is)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the embeddings folder
embedding_folder = os.path.join(current_dir, "embeddings")
os.makedirs(embedding_folder, exist_ok=True)

# Initialize components
processor = DocumentLoader()
embedor = EmbeddingGenerator()
llm = LLMClient()

st.write("📄 Upload your document to generate embeddings")
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file and st.button("🔄 Convert to Embeddings"):
    # Step 1: Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_pdf_path = tmp_file.name

    try:
        # Step 2: Process and generate embeddings
        chunks = processor.load_and_process(tmp_pdf_path)
        embedor.generate_embeddings(chunks, save_path=embedding_folder)
        st.success("✅ Embeddings generated and saved successfully!")
    finally:
        # Step 3: Clean up
        os.remove(tmp_pdf_path)

# User query section
user_query = st.text_input("Enter the symptoms you have that are to be diagnosed")
query_submission = st.button("Submit Query")

if user_query and query_submission:
    try:
        vector_store = embedor.load_vector_store(embedding_folder)
        similar_ones = vector_store.similarity_search(user_query, k=5)
        context = "\n\n".join([doc.page_content for doc in similar_ones])
        answer = llm.generate_output(context, user_query)
        st.markdown("### Diagnosis:")
        st.write(answer)
    except Exception as e:
        st.error(f"❌ Error: {e}")
