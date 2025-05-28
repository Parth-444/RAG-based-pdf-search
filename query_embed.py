from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
key = os.getenv("GOOGLE_API_KEY")
class QueryEmbeddingGenerator:

    def __init__(self):
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key= key
        )
    def embed_query(self, user_query):
        query_embeddings = self.embedding_model.embed_query(user_query)
        return query_embeddings