import streamlit as st
import google.generativeai as genai

# Initialize API token and set up model parameters
def initialize():
    """
    Initialize the configurations and clients using Streamlit secrets and session state.

    This function sets up the GitHub client, TiDB connection, Jina embedding model, and LLM.
    It handles the input of credentials and configurations from Streamlit's secrets or sidebar inputs.
    """
    if "GEMINI_API_KEY" in st.secrets:
        geminiai_api_key = st.secrets["GEMINI_API_KEY"]
    elif "gemini_api_key" in st.session_state:
        geminiai_api_key = st.session_state.gemini_api_key
    else:
        st.warning('Please provide Gemini API key in the sidebar.', icon="⚠️")
        st.stop()
    return geminiai_api_key

# Generate a response using gemini flask model
def generate_response(prompt):
    # Initialize the GenerativeModel
    gem_api_key = initialize()
    genai.configure(api_key=gem_api_key)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')

    # Define model parameters
    parameters = {
        "temperature": 0.7,  # Control randomness
        "max_tokens": 3072,   # Limit on the number of tokens generated
        "top_p": 0.9         # Nucleus sampling
    }
    response = model.generate_content(prompt, stream=True)

    return response