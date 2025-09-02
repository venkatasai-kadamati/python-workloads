from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model_name="mistral-small", max_tokens=100)

# ! simplest chatbot: without any memory
# while True:
#     user_input = input("You : ")
#     if user_input == "exit":
#         break
#     result = model.invoke(user_input)
#     print("AI : ", result.content)

# chat_history = []

# ! chatbot with memory - a new problem arises with this approach
# the chatbot will not be able to remember to which user input the AI is responding to, because the entire chat history is passed to the model at once
# while True:
#     user_input = input("You : ")
#     chat_history.append(user_input)
#     if user_input == "exit":
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("AI : ", result.content)
#
# print(chat_history)


# !  chatbot with memory - a better approach
# the chatbot will be able to remember to which user input the AI is responding to
chat_history = [SystemMessage(content="You are a helpful assistant.")]

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ", result.content)
print(chat_history)
