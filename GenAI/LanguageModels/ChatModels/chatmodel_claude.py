from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model="claude-3-5-sonnet-20241022")

chat_response = chat_model.invoke("Hi claude, how are you?")
print(chat_response)
