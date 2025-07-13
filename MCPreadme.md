# CloudPilot MCP (Fully Integrated with Copilot)


This documentation is intended for LLM agents, Copilot Coding Agent, and developers who want to interact with the Render MCP (Model Context Protocol) server. It describes the available endpoints, request/response formats, and integration notes for automated and programmatic use.

---

## **Instructions for LLMs and Agents: Endpoint Usage and Discovery**

### 1. How to Use Endpoints

- Always use `curl.exe` (not PowerShell's `curl` alias) to make HTTP requests to the MCP endpoints.
- All endpoints return plain JSON, suitable for automated parsing and reasoning.

**Example:**
```sh
curl.exe http://localhost:9000/render/services
```

### 2. How to Discover and Understand Endpoints

- To get a full, up-to-date list of all available endpoints and their details, fetch the OpenAPI JSON schema:

```sh
curl.exe http://localhost:9000/openapi.json
```

- This will return a machine-readable OpenAPI 3.1.0 specification describing every endpoint, its methods, parameters, and expected responses.
- LLMs and agents should parse this JSON to:
  - Enumerate all available endpoints (paths and methods)
  - Understand what each endpoint does (see the `summary`, `description`, and `operationId` fields)
  - Discover required parameters and request/response schemas

**Example for Endpoint Discovery:**
```sh
curl.exe http://localhost:9000/openapi.json
```

**How to interpret:**
- Each key in the `paths` object is an endpoint route.
- Each method (GET, POST, etc.) under a path describes the operation, parameters, and documentation.
- Use the `summary` and `description` fields to understand the purpose of each endpoint.

---

## Overview

This MCP server exposes Render.com cloud provider resources (services, databases, deploys, etc.) via a local HTTP API, following the Model Context Protocol (MCP) as described in [GitHub Copilot Coding Agent MCP Integration](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp).

- All endpoints return raw JSON from the upstream Render API for maximum compatibility.
- Authentication is handled via the `RENDER_API_KEY` environment variable.
- The server is designed for robust, automated, and agent-driven workflows.






## Example Endpoints

### Health
- `GET /v1/health` — Health check for the MCP server.

### Render Services
- `GET /render/services` — List all Render services.
- `GET /render/services/{serviceId}` — Get details for a specific service.
- `GET /render/services/{serviceId}/custom-domains` — List custom domains for a service.

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

## Agent Discovery: .mcp.json

To enable Copilot Coding Agent and other LLM agents to discover and interact with this MCP server, include a `.mcp.json` file in the project root. This file advertises the available tools (endpoints) and enables agent-driven automation.

**Example .mcp.json for full agent access:**
```json
{
  "tools": ["*"]
}
```

- The above configuration allows agents to access all MCP endpoints automatically.
- For more details, see the [GitHub Copilot Coding Agent MCP Integration](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp).


