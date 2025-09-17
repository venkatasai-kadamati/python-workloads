import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_mistralai import ChatMistralAI

# streamlit app to test dynamic prompting with a prompt Template
# using PromptTemplate method
load_dotenv()

model = ChatMistralAI(model_name="mistral-small", max_tokens=300)
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

template = load_prompt("Template.json")
prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    }
)


if st.button("Summarize"):
    model_result = model.invoke(prompt)
    st.write(model_result.content)
