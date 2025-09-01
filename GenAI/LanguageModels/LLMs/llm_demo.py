from langchain_openai import OpenAI
from dotenv import load_dotenv

# pulls all environment variables and makes them available
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

# invoke - an important function that takes in a prompt and returns a response
llm_result = llm.invoke("What is the capital of United States?")
print(llm_result)
