import streamlit as st
from LangGraph_backend import chatbot
from langchain_core.messages import HumanMessage,AIMessage
import uuid


# implementing session storage
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

# getting the messags from the session
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input=st.chat_input('type here')

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Generate a unique thread ID if not already present
    if 'thread_id' not in st.session_state:
        st.session_state['thread_id'] = str(uuid.uuid4())  # or use session ID, user ID, etc.

    # Get response from chatbot
    response = chatbot.invoke(
        {'messages': [HumanMessage(content=user_input)]},
        config={"thread_id": st.session_state['thread_id']}  # ← this line is required
    )

    ai_message = response['messages'][-1].content
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)