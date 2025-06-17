# legalAssistant/core/config.py

import os

# Application Settings
APP_TITLE = "Legal AI Assistant"
APP_ICON = "⚖️"
DEFAULT_LAYOUT = "wide"

# Provider Settings
SUPPORTED_PROVIDERS = ["fireworks", "ollama"]
DEFAULT_FIREWORKS_MODEL = "meta-llama/Llama-3.1-70B-Instruct"
DEFAULT_OLLAMA_MODEL = "llama3"

# API Keys - Must be set as environment variables
FIREWORKS_API_KEY = os.environ.get("FIREWORKS_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Default Context Template - Business Partnership Scenario
DEFAULT_CONTEXT_TEMPLATE = {
    "parties": "Partner A: 'Alex Chen', Partner B: 'Maria Rodriguez'",
    "scope": "50/50 partnership to start a restaurant business with shared investment and responsibilities",
    "location": "Texas, USA",
    "business_type": "Restaurant/Food Service",
    "investment": "Each partner contributing $50,000 for startup costs",
    "roles": "Alex handles operations, Maria handles marketing and customer relations"
}

# Default Task Template - Common Legal Request
DEFAULT_TASK_TEMPLATE = "Draft a partnership agreement with profit sharing, decision-making, and exit clauses for a restaurant business."

# Default Research Template - Relevant Legal Research
DEFAULT_RESEARCH_TEMPLATE = "Texas partnership agreement requirements restaurant business 2024"

# Research Settings
MAX_SEARCH_RESULTS = 5
SEARCH_DEPTH = "advanced"

# UI Settings
CONTEXT_TEXTAREA_HEIGHT = 150
BUTTON_TYPE = "primary"
BUTTON_USE_CONTAINER_WIDTH = True 