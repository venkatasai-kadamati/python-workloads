from langchain_openai import ChatOpenAI
# inherits from BaseChatModel
from dotenv import load_dotenv

load_dotenv()

# temperate ranges from 0 to 2. simply put, how much randomness we want in our output
# max_completion_tokens is the maximum number of tokens we want in our output
chat_model = ChatOpenAI(model="gpt-4", temperature=0.9, max_completion_tokens=100)

# conceptually we need to understand the runnable interface
chat_result = chat_model.invoke("Hello, how are you?")

# unlike llms, which have string output, chat models have lots of options like content (our actual output), additional kwargs, etc.
print(chat_result.content)
