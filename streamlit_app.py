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
DESC_02 = """
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
    
DESC_03 = """
Use the with statement to confine the constituent contents to the sidebar. They include:

The app title is specified via st.title()
A short description of the app via st.markdown()
Vertical space added via add_vertical_space() method from streamlit-extras
A short credit message via st.write()
"""
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

DESC_04 = """
Here, past denotes the human user's input and generated indicates the bot's response.
"""

DESC_05 = """
5. App layout
Give the app a general layout. The main panel will display the chat query and responses:
"""
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()
Use st.container() as a placeholder where the input_container and response_container variables correspond to the human user and chatbot, respectively.

DESC_06 = """
6. Human user input
Create the get_text() custom function that will take prompts provided by the human user as input using st.text_input(). This custom function displays a text box in the input_container:
"""
# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()
DESC_07 = """
7. Bot response output
Create the generate_response(prompt) custom function for taking in the user's input prompt as an argument to generate an AI response using the HuggingChat API via the hugchat.ChatBot() method (this LLM model can be swapped with any other one):
"""
# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response
DESC_07_1 = """
Populate the response_container with the AI-generated response with the two underlying if statements:

If the user has entered their input query, the if user_input statement will become True and the underlying statements will run.
The user-provided prompt (user_input) will serve as an input argument to generate_response() to make the AI-generated response.
Subsequently, the generated output will be assigned to the response variable.
Both values for user_input and response will be saved to the session state via the append() method.
When there are bot-generated messages, the if st.session_state['generated'] statement returns True and the underlying statements will run.
A for loop iterates through the list of generated messages in st.session_state['generated']
The human (st.session_state['past']) and the bot (st.session_state['generated']) messages are displayed via the message() command from the streamlit-chat component:
"""
## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
