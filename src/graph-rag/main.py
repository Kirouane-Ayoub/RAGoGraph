import streamlit as st

st.set_page_config(page_title="Graph RAG Chatbot")
st.header(":hand: Welcome To Graph RAG Chatbot ")
st.write(
    """

"""
)

with st.sidebar:
    temperature = st.sidebar.slider(
        "Select your temperature value : ", min_value=0.1, max_value=1.0, value=0.5
    )


def run_qa(prompt):
    return prompt


if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi :hand: Im your Graph chatbot. How may I help you?",
        }
    ]
# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_qa(prompt)
            placeholder = st.empty()
            full_response = ""
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
