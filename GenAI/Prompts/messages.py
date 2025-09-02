from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model_name="mistral-small", max_tokens=100)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)
