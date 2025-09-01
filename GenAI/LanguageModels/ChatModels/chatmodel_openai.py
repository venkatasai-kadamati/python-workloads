from langchain_openai import ChatOpenAI
# inherits from BaseChatModel
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4")

# conceptually we need to understand the runnable interface
chat_result = chat_model.invoke("Hello, how are you?")

# unlike llms, which have string output, chat models have lots of options like content (our actual output), additional kwargs, etc.
print(chat_result.content)
