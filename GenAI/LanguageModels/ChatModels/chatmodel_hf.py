from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task="text-generation",
)
chat_model = ChatHuggingFace(llm=llm)

chat_response = chat_model.invoke("What is the capital of India?")
print(chat_response)
