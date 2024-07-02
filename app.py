from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st

# FUnction for response 

def get_openai_response(query):
    llm = OpenAI(model_name = "gpt-3.5-turbo",temperature=0.5)
    response = llm(query)
    return response


#Streamlit code 

st.set_page_config(page_title="ASK ME ANYTHING ! ")
st.header("Welcome to AMAN_GPT")

input = st.text_input("Input : ",key ="input")
get_openai_response(input)
submit = st.button('Ask your question.')

# If button pressed 

if submit:
    st.subheader("The response for your question is : ")
    st.write(get_openai_response(input))