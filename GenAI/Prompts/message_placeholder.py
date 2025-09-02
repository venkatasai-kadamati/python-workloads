from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_history = []
# step1: load chat history
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# step2: chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent"),
        # inject the old history for context
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)


# create prompt
prompt = chat_template.invoke(
    {"chat_history": chat_history, "query": "Where is my refund"}
)

print(prompt)
