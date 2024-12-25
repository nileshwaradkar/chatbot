from langchain_ollama.chat_models import ChatOllama
import streamlit as st

# Initialize the ChatOllama model with the correct base URL
# Replace "http://localhost:11434" with the correct URL if the server is hosted elsewhere
llm = ChatOllama(model="llama3.1", base_url="http://localhost:11434")

# Streamlit app
st.title("Chatbot")

# Initialize session state
if "model" not in st.session_state:
    st.session_state.model = "llama3.1"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=":material/person:" if message["role"] == "human" else "ai"):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Enter your message: "):
    st.session_state.messages.append({"role": "human", "content": prompt})
    with st.chat_message("human",avatar=":material/person:"):
        st.markdown((prompt))
        
    # Generate AI response
    with st.chat_message("ai"):
        try:
            response = llm.invoke(prompt).content
        except Exception as e:
            response = "There was an error processing your request. Please try again later."
            st.error(f"Error: {e}")
        
        st.markdown(response)

    # Append AI response
    st.session_state.messages.append({"role": "ai", "content": response})

