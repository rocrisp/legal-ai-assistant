# legalAssistant/core/ui_components.py

import streamlit as st
import json
from .config import (
    APP_TITLE,
    APP_ICON,
    DEFAULT_LAYOUT,
    SUPPORTED_PROVIDERS,
    DEFAULT_OLLAMA_MODEL,
    DEFAULT_CONTEXT_TEMPLATE,
    DEFAULT_TASK_TEMPLATE,
    DEFAULT_RESEARCH_TEMPLATE,
    CONTEXT_TEXTAREA_HEIGHT,
    BUTTON_TYPE,
    BUTTON_USE_CONTAINER_WIDTH
)

def setup_page_config():
    """Sets up the Streamlit page configuration."""
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout=DEFAULT_LAYOUT,
    )
    st.title(f"{APP_ICON} {APP_TITLE} Workflow")

def setup_sidebar():
    """Sets up the sidebar configuration and returns provider settings."""
    st.sidebar.header("Configuration")
    provider = st.sidebar.selectbox("Select Inference Provider", SUPPORTED_PROVIDERS)

    ollama_model = None
    if provider == "ollama":
        ollama_model = st.sidebar.text_input("Enter Ollama Model Name", DEFAULT_OLLAMA_MODEL)
    
    return provider, ollama_model

def get_default_context():
    """Returns the default context JSON for the text area."""
    return json.dumps(DEFAULT_CONTEXT_TEMPLATE, indent=2)

def render_input_forms():
    """Renders the main input forms and returns user inputs."""
    st.header("1. Define the Legal Task")
    task_input = st.text_input(
        "**Enter the primary drafting goal:**",
        DEFAULT_TASK_TEMPLATE
    )

    st.header("2. Provide Context")
    context_input = st.text_area(
        "**Enter context as a JSON object:**",
        get_default_context(),
        height=CONTEXT_TEXTAREA_HEIGHT
    )

    st.header("3. (Optional) Add a Research Topic")
    research_input = st.text_input(
        "**Enter a topic for the Research Agent:**",
        DEFAULT_RESEARCH_TEMPLATE
    )

    return task_input, context_input, research_input

def render_generate_button():
    """Renders the generate button and returns True if clicked."""
    return st.button(
        "🚀 Generate Legal Drafts", 
        type=BUTTON_TYPE, 
        use_container_width=BUTTON_USE_CONTAINER_WIDTH
    )

def display_error(message):
    """Displays an error message."""
    st.error(message)

def display_warning(message):
    """Displays a warning message."""
    st.warning(message)

def display_success(message):
    """Displays a success message."""
    st.success(message) 