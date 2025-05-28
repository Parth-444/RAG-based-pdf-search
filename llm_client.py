from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from nltk.sentiment.util import output_markdown
import os

def get_llm():
    key = os.getenv('GOOGLE_API_KEY')
    return ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=key)


class LLMClient:
    def __init__(self):
        self.llm = get_llm()

    def get_prompt(self):
        return PromptTemplate(
        template="""
            You are an assistant. Use the following information to answer the user's question.
            
            Context:
            {context}
            
            Question:
            {user_query}
            
            Answer:""",
            input_variables=["context", "user_query"],
        )

    def generate_output(self, context, user_query):
        prompt=self.get_prompt()
        chain = prompt | self.llm
        result = chain.invoke({"context":context, "user_query":user_query})
        return result.content
