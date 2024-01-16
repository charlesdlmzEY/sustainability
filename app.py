from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI
import requests
import os
import streamlit as st
import openai 

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    st.set_page_config(page_title="img 2 audio story", page_icon ="Hey")

    st.header("💬 Chatbot")
    
    with st.sidebar:
        st.selectbox('Select', ["RSE","Réglementation"])
 
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not OPENAI_API_KEY:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()
        else : 
            openai.api_key = OPENAI_API_KEY
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
            msg = response.choices[0].message
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(msg.content)


if __name__ == '__main__':
    main()