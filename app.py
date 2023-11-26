# Q&A ChatBot
from langchain.llms import OpenAI 
from dotenv import load_dotenv

load_dotenv() # take environment varialbes from .env

import streamlit as st
import os


## Function to load OpenAi model and get responses

def get_open_response(question):
    llm= OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="text-davinci-003", temperature=0.5)
    response=llm(question)
    return response

## Initialise our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input:  ", key="input")
response = get_open_response(input)
submit = st.button("Generate")

## If Generate button is clicked

if submit:
    st.subheader("The Reponse is")
    st.write(response)
