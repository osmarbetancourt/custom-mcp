

# CloudPilot MCP — Internal Development README

This README is for internal use only. Use it to track:

## Project Overview / Architecture

CloudPilot MCP is a Model Context Protocol (MCP) server that exposes cloud provider resources (currently Render.com, with planned support for GCP, Azure, AWS) via a local HTTP API. It is designed for robust, agent-driven automation and seamless integration with GitHub Copilot Coding Agent and LLMs.

**Key Features:**
- Exposes REST endpoints for listing, creating, and deleting cloud resources (services, databases, deploys, etc.)
- Returns raw JSON from upstream cloud APIs for maximum compatibility
- Handles authentication via environment variables (e.g., `RENDER_API_KEY`)
- Agent/LLM discoverability via `.mcp.json` and agent-oriented documentation (`MCPreadme.md`)
- Designed to be packaged as a standalone executable for easy use in any project folder

**Main Components:**
- `main.py`: FastAPI app implementing all MCP and cloud provider endpoints
- `models.py`: Pydantic models for request/response validation
- `.mcp.json`: Advertises available endpoints/tools for agent discovery
- `MCPreadme.md`: Agent/LLM-oriented documentation for endpoints and usage
- `README.md`: Internal dev notes, release control, and architecture (this file)

**How it works:**
1. User places `.mcp.json` (and optionally `MCPreadme.md`) in their project folder
2. User runs the CloudPilot MCP executable or script in that folder
3. The MCP server loads config/credentials, starts up, and exposes HTTP endpoints for agent or developer use
4. Agents (e.g., Copilot Coding Agent) discover and interact with the MCP via `.mcp.json` and the documented endpoints

**Extensibility:**
- New cloud providers can be added by implementing additional endpoints and models
- The MCP can be packaged and distributed as a binary, with only minimal files required in the user’s project

**Security:**
- Credentials are loaded from environment variables or config files, not hardcoded
- Only the executable and public docs are released; source code remains private until open source

See `MCPreadme.md` for endpoint details and agent-facing docs.
- Release notes and version history
- Bug reports and fixes
- Development roadmap and TODOs
- Build/package instructions
- Internal notes and decisions

## Release Notes
- v0.1.0 — Initial private release, Render.com support, Copilot integration, agent discovery via .mcp.json

## Bug Reports / Fixes
- [ ] (Add bugs and fixes here)

## Roadmap / TODO
- [ ] Add GCP, Azure, AWS support
- [ ] Package as standalone executable (PyInstaller)
- [ ] Add CLI interface
- [ ] Improve error handling and logging

## Build/Packaging Instructions
1. Ensure all dependencies are installed (see requirements.txt)
2. To build executable: `pyinstaller --onefile start.py` (update as needed)
3. Release only the executable and public docs to the public repo

## Internal Notes
- Keep this repo private until ready for open source
- Public repo should only contain the executable, MIT license, and minimal usage docs

---
For user/agent documentation, see MCPreadme.md
