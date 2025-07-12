# MCP API for Render Cloud Provider

This documentation is intended for LLM agents, Copilot Coding Agent, and developers who want to interact with the Render MCP (Model Context Protocol) server. It describes the available endpoints, request/response formats, and integration notes for automated and programmatic use.

## Overview

This MCP server exposes Render.com cloud provider resources (services, databases, deploys, etc.) via a local HTTP API, following the Model Context Protocol (MCP) as described in [GitHub Copilot Coding Agent MCP Integration](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp).

- All endpoints return raw JSON from the upstream Render API for maximum compatibility.
- Authentication is handled via the `RENDER_API_KEY` environment variable.
- The server is designed for robust, automated, and agent-driven workflows.

## Endpoints

### Health
- `GET /v1/health` — Health check for the MCP server.

### Render Services
- `GET /render/services` — List all Render services.
- `GET /render/services/{serviceId}` — Get details for a specific service.
- `GET /render/services/{serviceId}/custom-domains` — List custom domains for a service.
- `GET /render/services/{serviceId}/deploys` — List deploys for a service.
- `GET /render/services/{serviceId}/env-vars` — List environment variables for a service.
- `POST /render/services` — Create a new Render service (see models for required fields).

### Render Databases
- `GET /render/databases` — List all database services.
- `GET /render/databases/{databaseId}` — Get details for a specific database.
- `POST /render/create-db` — Create a new PostgreSQL database. Required fields:
  - `name` (str): Database name
  - `region` (str, e.g. 'oregon')
  - `plan` (str, e.g. 'free', 'starter')
  - `ownerId` (str): Team or user ID
  - `version` (str, e.g. '13')
- `DELETE /render/databases/{databaseId}` — Delete a database by ID.

### Render Deploys
- `GET /render/deploys/{deployId}` — Get details for a specific deploy.

### MCP Protocol Endpoints
- `POST /v1/context` — (Stub) For MCP context requests.
- `POST /v1/search` — (Stub) For MCP search requests.

## Authentication
- All requests to the Render API require the `RENDER_API_KEY` to be set in the environment.
- The MCP server will return a 500 error if the key is missing.

## Example: Creating a Database
```json
{
  "name": "db-by-copilot",
  "region": "oregon",
  "plan": "free",
  "ownerId": "<your-owner-id>",
  "version": "13"
}
```

## Example: Deleting a Database
- Send a DELETE request to `/render/databases/{databaseId}` with the database ID.

## Integration Notes
- This MCP server is designed to be used by LLM agents and Copilot Coding Agent for automated cloud resource management.
- All endpoints return raw JSON for maximum compatibility and robustness.
- For more details on the MCP protocol, see [GitHub Copilot Coding Agent MCP Integration](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp).

---

This documentation is for agent and automation use. For human-friendly docs, see the main project README or the Render API docs.
