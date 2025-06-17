# Legal Assistant AI

This Streamlit application uses a multi-agent system to handle legal drafting tasks.

## About This Project

This project is based on the [Llama Stack Agent Workflows notebook](https://github.com/meta-llama/llama-stack/blob/main/docs/notebooks/Llama_Stack_Agent_Workflows.ipynb) from Meta's Llama Stack repository. It demonstrates how to build multi-agent workflows using Llama Stack for legal document generation and research.

## Prerequisites

### Required Software

1. **Python 3.8+**: Ensure you have Python 3.8 or higher installed
2. **Ollama** (if using local models): Install Ollama for local AI model inference

### API Keys Required

This application requires API keys for certain features:

1. **Fireworks AI API Key** (for cloud-based AI models):
   - Get your key from: https://console.fireworks.ai/
   - Required for: Cloud AI model inference

2. **Tavily API Key** (for web search functionality):
   - Get your key from: https://tavily.com/
   - Required for: Legal research and web search

### Setting Up Environment Variables

1. **Copy the example file:**
   ```bash
   cp env.example .env
   ```

2. **Edit the .env file** with your actual API keys:
   ```bash
   # Fireworks AI API Key
   FIREWORKS_API_KEY=your_actual_fireworks_key_here
   
   # Tavily API Key
   TAVILY_API_KEY=your_actual_tavily_key_here
   ```

3. **Load the environment variables:**
   ```bash
   # macOS/Linux
   export $(cat .env | xargs)
   
   # Or set them manually:
   export FIREWORKS_API_KEY="your_key_here"
   export TAVILY_API_KEY="your_key_here"
   ```

**Note**: If you're only using Ollama (local models), you don't need the Fireworks API key.

### Installing Ollama

**macOS:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download and install from: https://ollama.ai/download

### After Installing Ollama

1. **Start Ollama service:**
   ```bash
   ollama serve
   ```

2. **Pull a model** (e.g., Llama 3):
   ```bash
   ollama pull llama3
   ```

3. **Verify installation:**
   ```bash
   ollama list
   ```

## Setup

1.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

2.  **Activate the Environment:**
    * **macOS/Linux:** `source venv/bin/activate`
    * **Windows:** `venv\Scripts\activate`

3.  **Install Dependencies:**
    Make sure you are in the `virtual_agent` directory, then run:
    ```bash
    pip install -r requirements.txt
    ```

     **Note for Ollama Users:**
    If you plan to use the `ollama` or the `fireworks` provider, you must run the following Llama Stack command. This command sets up the necessary configuration for Llama Stack to communicate with your local Ollama instance.

    ```bash
    UV_SYSTEM_PYTHON=1 llama stack build --template fireworks --image-type venv
    UV_SYSTEM_PYTHON=1 llama stack build --template ollama --image-type venv
    ```

## Running the Application

Ensure your virtual environment is active and you are in the `virtual_agent` directory. Then, run the following command:

```bash
streamlit run app.py
```

## Usage

1. **Select Provider**: Choose between "fireworks" (cloud) or "ollama" (local) in the sidebar
2. **Model Selection**: If using Ollama, specify the model name (e.g., "llama3", "qwen2:7b")
3. **Enter Task**: Describe the legal document you want to create
4. **Provide Context**: Add relevant details about parties, scope, and location
5. **Optional Research**: Add a research topic for additional legal insights
6. **Generate**: Click "Generate Legal Drafts" to create your documents

## Troubleshooting

**API Key Issues:**
- Ensure environment variables are set: `echo $FIREWORKS_API_KEY`
- Check if .env file is loaded correctly
- Verify API keys are valid and have sufficient credits

**Ollama Connection Issues:**
- Ensure Ollama service is running: `ollama serve`
- Check if model is available: `ollama list`
- Verify Ollama is accessible: `curl http://localhost:11434/api/tags`

## References

- **Llama Stack Agent Workflows**: [https://github.com/meta-llama/llama-stack/blob/main/docs/notebooks/Llama_Stack_Agent_Workflows.ipynb](https://github.com/meta-llama/llama-stack/blob/main/docs/notebooks/Llama_Stack_Agent_Workflows.ipynb)
- **Llama Stack Documentation**: [https://github.com/meta-llama/llama-stack](https://github.com/meta-llama/llama-stack)
