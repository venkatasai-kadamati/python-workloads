import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# streamlit app to test static prompting
load_dotenv()

model = ChatMistralAI(model_name="mistral-small", max_tokens=100)
st.header("Research Tool")

user_query = st.text_input("Enter your prompt")

if st.button("Summarize"):
    model_result = model.invoke(user_query)
    st.write(model_result.content)
