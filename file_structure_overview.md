## Overview
## File Structure

```
virtual_agent/
├── app.py                          # Main application entry point
├── core/                           # Core application modules
│   ├── __init__.py
│   ├── client.py                   # Client initialization
│   ├── config.py                   # Centralized configuration
│   ├── ui_components.py            # UI components and forms
│   ├── validation.py               # Input validation
│   └── workflow.py                 # Main workflow logic
├── agents/                         # AI agent configurations
│   ├── __init__.py
│   ├── config.py                   # Agent configurations
│   └── research.py                 # Research functionality
└── requirements.txt                # Dependencies
```

## Module Descriptions

### 📁 **app.py** - Main Entry Point
- **Purpose**: Application entry point and main orchestration
- **Responsibilities**:
  - Import and initialize modules
  - Handle main application flow
  - Coordinate between different components

### 📁 **core/client.py** - Client Management
- **Purpose**: Initialize and manage AI model clients
- **Responsibilities**:
  - Create LlamaStack client connections
  - Handle provider-specific configurations
  - Manage API keys and environment variables

### 📁 **core/config.py** - Configuration Management
- **Purpose**: Centralized configuration and constants
- **Responsibilities**:
  - Define application settings
  - Store API keys and defaults
  - Manage UI configuration
  - Provide templates and constants

### 📁 **core/ui_components.py** - User Interface
- **Purpose**: Streamlit UI components and forms
- **Responsibilities**:
  - Page configuration
  - Sidebar setup
  - Input form rendering
  - Display functions (error, warning, success)

### 📁 **core/validation.py** - Input Validation
- **Purpose**: Validate user inputs and system state
- **Responsibilities**:
  - Validate form inputs
  - Check JSON format
  - Verify model selection
  - Ensure client initialization

### 📁 **core/workflow.py** - Business Logic
- **Purpose**: Main workflow execution logic
- **Responsibilities**:
  - Research phase execution
  - Orchestration phase execution
  - Drafting phase execution
  - Workflow coordination

### 📁 **agents/config.py** - Agent Configurations
- **Purpose**: Define AI agent behaviors and instructions
- **Responsibilities**:
  - Legal orchestrator configuration
  - Research agent configuration
  - Legal worker agent configuration
  - Output schemas and formats

### 📁 **agents/research.py** - Research Functionality
- **Purpose**: Execute legal research tasks
- **Responsibilities**:
  - Web search integration
  - Query generation
  - Result summarization
  - Insight extraction
