# legalAssistant/app.py

import os
# Disable OpenTelemetry to prevent import errors
os.environ['OTEL_PYTHON_DISABLED'] = 'true'

import streamlit as st

# Local imports from our modular structure
from core.client import init_client
from core.ui_components import (
    setup_page_config,
    setup_sidebar,
    render_input_forms,
    render_generate_button,
    display_error,
    display_warning
)
from core.workflow import run_legal_workflow
from core.validation import (
    validate_inputs,
    validate_json_context,
    validate_model_selection,
    validate_client_initialization
)

def main():
    """Main application function."""
    # Setup page configuration
    setup_page_config()
    
    # Setup sidebar and get provider settings
    provider, ollama_model = setup_sidebar()
    
    # Initialize the client
    client = init_client(provider, ollama_model)
    
    # Validate client initialization
    if not validate_client_initialization(client):
        return
    
    # Render input forms
    task_input, context_input, research_input = render_input_forms()
    
    # Handle generate button click
    if render_generate_button():
        # Validate inputs
        if not validate_inputs(task_input, context_input):
            return
        
        # Validate and parse JSON context
        context_data = validate_json_context(context_input)
        if context_data is None:
            return
        
        # Validate model selection
        model_id = validate_model_selection(provider, ollama_model)
        if model_id is None:
            return
        
        # Run the legal workflow
        run_legal_workflow(client, task_input, context_data, research_input, model_id)

if __name__ == "__main__":
    main()
