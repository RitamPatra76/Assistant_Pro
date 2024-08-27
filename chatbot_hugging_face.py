import streamlit as st
from transformers import pipeline
chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill")

st.title("Assistant pro")
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Add a welcome message
    welcome_message = "Welcome to the chat! How can I assist you today?"
    st.session_state.messages.append({"role": "bot", "content": welcome_message})
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):

    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = chatbot(prompt)[0]['generated_text']
  
    with st.chat_message("bot"):
        st.markdown(response)
    st.session_state.messages.append({"role": "bot", "content": response})
