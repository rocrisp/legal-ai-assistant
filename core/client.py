# legalAssistant/core/client.py

import os
# Disable OpenTelemetry to prevent import errors
os.environ['OTEL_PYTHON_DISABLED'] = 'true'

import streamlit as st
from llama_stack.distribution.library_client import LlamaStackAsLibraryClient
from .config import FIREWORKS_API_KEY

@st.cache_resource
def init_client(provider_name: str, ollama_model_name: str = None):
    """
    Initializes the LlamaStack client based on the selected provider.
    """
    try:
        if provider_name == "ollama":
            if not ollama_model_name:
                st.warning("Please provide an Ollama model name in the sidebar.")
                return None
            # Set the environment variable required by the ollama provider
            os.environ['INFERENCE_MODEL'] = ollama_model_name
            client = LlamaStackAsLibraryClient("ollama")
        else:  # Default to fireworks
            if not FIREWORKS_API_KEY:
                st.error("FIREWORKS_API_KEY environment variable is not set. Please set it before running the application.")
                st.info("You can set it by running: export FIREWORKS_API_KEY='your_api_key_here'")
                return None
            client = LlamaStackAsLibraryClient("fireworks", provider_data={"fireworks_api_key": FIREWORKS_API_KEY})

        _ = client.initialize()
        return client
    except Exception as e:
        st.error(f"Failed to initialize LlamaStack client: {e}")
        return None
