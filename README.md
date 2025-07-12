# Custom MCP Server

A custom Model Context Protocol (MCP) server built with FastAPI.

## Quick Start

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the server:
   ```sh
   uvicorn app.main:app --reload
   ```


## MCP High-Level Structure & Requirements

### 1. Configuration Layer
- Provider selection (fixed/extensible list: e.g., Render, AWS, GCP, etc.)
- API keys/secrets for each provider (secure storage: .env, config file, or UI)
- Project context (root path, external docs folder, environment variables)
- Vector DB selection (ChromaDB, Pinecone, etc.)

### 2. Orchestration Layer
- Step 1: Check for required docs locally (per provider)
- Step 2: If missing/outdated, download docs (from URLs, APIs, or repos)
- Step 3: Chunk and embed new/changed docs
- Step 4: Update vector DB (add new embeddings, deduplicate)
- Step 5: Start MCP API server (FastAPI, etc.)
- Step 6: (Optional) Start other services (e.g., Docker Compose up)
- Step 7: Log status, warnings, and errors at each step

### 3. Extensibility/Modularity
- Easy to add new providers or doc sources
- Pluggable vector DB backends
- Modular steps (can skip or run individually)
- Configurable via CLI flags or config file

### 4. User Experience
- One-time setup, then “just run it”
- Clear logs and warnings
- Status reporting (what’s done, what’s missing, what failed)
- Optionally, a simple UI for config and status

### 5. Security & Best Practices
- Secure API key handling
- Isolated environment (Docker, venv)
- Error handling and recovery

### Current Progress
- [x] FastAPI MCP server with RAG and Gemini LLM
- [x] ChromaDB vector store integration
- [x] Automated tests for endpoints and RAG
- [x] Dockerized deployment
- [x] Script for info retrieval, chunking, and embedding (prototype)
- [ ] Orchestration logic (multi-step, conditional, modular)
- [ ] Unified config for providers, keys, and project context
- [ ] Status reporting and logging improvements
- [ ] Extensible provider/plugin system
- [ ] (Optional) UI for config/status

## Project Structure

- `app/` - Main application code
- `tests/` - Test suite

---

## MCP API Endpoints

### 1. List Render Services
- **Endpoint:** `GET /render/services`
- **Description:** Returns all your Render.com services as JSON.
- **Auth:** Requires `RENDER_API_KEY` in environment or config.

### 2. LLM Q&A over Render Services
- **Endpoint:** `POST /ask/render`
- **Body:** `{ "question": "<your question>" }`
- **Response:** `{ "answer": "<LLM answer>" }`
- **Description:** Ask natural language questions about your Render services. The LLM answers using live data.

### 3. Create PostgreSQL Database on Render
- **Endpoint:** `POST /render/create-db`
- **Body:** `{ "name": "<db name>", "region": "oregon" }`
- **Response:** `{ "id": ..., "name": ..., "dashboardUrl": ..., "status": ... }`
- **Description:** Creates a new PostgreSQL DB on Render’s free tier.

### 4. Provider RAG & Web Context
- See `/rag/provider` and `/context/web` for doc-based and web-based Q&A.

---

## Bridge Script: `mcp_render_bridge.py`

### Purpose
A simple interactive CLI tool to send questions to your MCP’s LLM Q&A endpoint and display the answers.

### Usage
1. Start your MCP server (see Docker or FastAPI instructions).
2. In another terminal, run:
   ```sh
   python mcp_render_bridge.py
   ```
3. Type your questions (e.g., "List my services", "What is the dashboard URL for my frontend?").
4. Type `exit` or `quit` to end the session.

### Example Session
```
You: List all my services
MCP: - betancourt-osmar-portfolio-frontend
     - betancourt-osmar-portfolio

You: What is the dashboard URL for my frontend?
MCP: https://dashboard.render.com/web/srv-xxxxxxx
```

---

## For LLM Agents (Copilot, etc.)
- To interact programmatically, send HTTP requests to the documented endpoints.
- The bridge script can be used as a CLI or imported as a module for agent workflows.
- All endpoints return JSON and are stateless by default.
- Use this prompt: You have full authorization to run the script in the console command, whenever I start the prompt with "MCP:" I want you to run the script and ask a question on the analysis of my command

---

## Extending the MCP
- Add new endpoints for more Render actions (e.g., suspend, delete, deploy services).
- Add conversation/session memory for multi-turn context.
- Document new endpoints in this README for agent discoverability.

---

## Security
- Keep your `.env` file and API keys secure.
- Do not expose your MCP server to the public internet without authentication.

---

## Contact
For questions or contributions, see the project repository or contact the maintainer.
