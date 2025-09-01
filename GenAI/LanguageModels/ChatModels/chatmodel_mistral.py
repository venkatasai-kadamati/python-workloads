from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatMistralAI(model="mistral-small", max_tokens=10)

chat_response = chat_model.invoke("What is the capital of India?")
print("mistal answers: " + "\n " + chat_response.content)
