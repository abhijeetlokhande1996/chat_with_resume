import streamlit as st
from streamlit_chat import message
from chat_bot import chat_with_model

if ("chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state):
    
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []

st.header("Chat with me (AL_Resume)")

prompt = st.text_input(label="Prompt", placeholder="enter your message here..") or st.button("submit")

if prompt:
    with st.spinner("Generating Response.."):
        generated_response = chat_with_model(question=prompt, chat_history=st.session_state["chat_history"])
        st.session_state["chat_history"].append((prompt, generated_response["answer"]))
        
        formatted_response = (
            f"{generated_response['answer']}\n"
        )
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["user_prompt_history"].append(prompt)

if st.session_state["chat_answers_history"]:
    index = 0
    for answer, user_query in zip(st.session_state["chat_answers_history"], st.session_state["user_prompt_history"]):
        message(user_query, is_user=True, key=index)
        index+=1
        message(answer, key=index)
        index+=1


