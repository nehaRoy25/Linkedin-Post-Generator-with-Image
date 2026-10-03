from langchain_groq import ChatGroq
import streamlit as st

GROQ_API_KEY=st.secrets["GROQ_API_KEY"]
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="openai/gpt-oss-120b")


if __name__ == "__main__":  # This is just for testing
    response = llm.invoke("tell me about llm")
    print(response.content)





