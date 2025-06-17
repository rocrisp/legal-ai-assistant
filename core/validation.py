# legalAssistant/core/validation.py

import json
import streamlit as st
from .config import DEFAULT_FIREWORKS_MODEL

def validate_inputs(task_input, context_input):
    """Validates that required inputs are provided."""
    if not task_input or not context_input:
        st.error("Please ensure the Task and Context fields are filled out.")
        return False
    return True

def validate_json_context(context_input):
    """Validates that the context input is valid JSON."""
    try:
        context_data = json.loads(context_input)
        return context_data
    except json.JSONDecodeError:
        st.error("Invalid JSON in context. Please check the format.")
        return None

def validate_model_selection(provider, ollama_model):
    """Validates that a valid model is selected."""
    if provider == 'ollama' and not ollama_model:
        st.warning("Please provide an Ollama model name in the sidebar.")
        return None
    
    model_id = ollama_model if provider == 'ollama' else DEFAULT_FIREWORKS_MODEL
    return model_id

def validate_client_initialization(client):
    """Validates that the client is properly initialized."""
    if not client:
        st.error("LlamaStack Client could not be initialized. Check your configuration and ensure the service is running.")
        return False
    return True 