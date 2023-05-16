DESC_01 = """
1. Required libraries
Import prerequisite Python libraries:
"""
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
st.title(🥸 Grouchat)
DESC_2 = """
2. Page config
Name the app using the page_title input argument in the st.set_page_config method (it'll be used as the app title and as the title in the preview when sharing on social media):
"""
st.set_page_config(page_title="🥸 Grouchat using HugChat - An LLM-powered Streamlit app")

with st.sidebar:
    st.title('🥸💬 Grouchat® using HugChat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Data Professor](<https://youtube.com/dataprofessor>)')
