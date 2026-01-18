# How to Install Ollama

Ollama is a tool to run LLMs locally on your machine.

## Installation
1. Download the installer from [https://ollama.com/download](https://ollama.com/download).
2. Run the installer application.
3. Open a terminal and verify installation:
   ```bash
   ollama --version
   ```

## Usage
1. Pull a model (e.g., Llama 3):
   ```bash
   ollama pull llama3
   ```
2. Run the model to test:
   ```bash
   ollama run llama3
   ```
3. The server runs automatically in the background at `http://localhost:11434`.

## Using with this Project
1. Set `LLM_API_KEY=ollama` in `.env`.
2. Set `LLM_BASE_URL=http://localhost:11434/v1` in `.env`.
3. Set `LLM_MODEL=llama3` (or whatever model you pulled) in `.env`.
