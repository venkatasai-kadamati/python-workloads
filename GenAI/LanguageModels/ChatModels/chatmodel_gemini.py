from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.5, max_tokens=100)

chat_response = chat_model.invoke("What is the current situation with india, russia, china and usa?")
print(chat_response.content)
