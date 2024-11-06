#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install ollama


# In[3]:


import streamlit as st
import ollama
import time

def stream_data(text, delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)

# Input for the prompt
prompt = st.chat_input("Ask Anything")

if prompt:
    # Display input prompt from user
    with st.chat_message("user"):
        st.write(prompt)

    # Processing
    with st.spinner("Thinking ..."):
        result = ollama.chat(model="tinyllama", messages=[{
            "role": "user",
            "content": prompt,
        }])

    response = result["message"]["content"]
    st.write_stream(stream_data(response))


# In[ ]:




