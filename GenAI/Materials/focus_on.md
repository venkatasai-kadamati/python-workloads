### Understand memory & types including the 2 ways to define it

> method 1: using AIMessage, HumanMessage & SystemMessage

```python
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?"),
]

result = model.invoke(messages)
```

> method 2: using just passable parameters like role, content

```python
chat_template = ChatPromptTemplate(
        [
            ("system", "You are a helpful customer support agent"),
            # inject the old history for context
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{query}"),
        ]
)
```

###  