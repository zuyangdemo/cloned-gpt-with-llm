import os

import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import generate_search_result

st.header("万能AI助手")

with st.sidebar:
    openai_api_key = st.text_input(label="请输入你的API key", value=os.getenv("OPENAI_API_KEY"), type="password")
    st.markdown("[获取OPENAI API KEY](https://openai.com/)")

if "memory" not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(return_messages=True)
    st.session_state['messages'] = [{"role": "ai", "content": "请给出你的问题和一些耐心，我会尽力回答...💗"}]

for message in st.session_state['messages']:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入OPENAI API KEY")
        st.stop()

    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("AI 正在思索中，请稍后..."):
        result = generate_search_result(prompt, st.session_state['memory'], openai_api_key)
    st.session_state["messages"].append({"role": "ai", "content": result})
    st.chat_message("ai").write(result)
