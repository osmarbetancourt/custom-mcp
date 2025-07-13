# Custom Render MCP Server

**A foundation for AI-driven automation and agent integration.**

This project is a robust, extensible template for building advanced Model Context Protocol (MCP) servers that bridge modern AI agents (like GitHub Copilot) with any API-powered service. Here, the Render.com API is fully exposed as a suite of MCP tools—enabling seamless, programmatic control of your cloud resources through natural language and agent workflows.


**What does this enable?**

- Use AI agents to automate, orchestrate, and manage your cloud resources or any API-driven service.
- Instantly expose your API as a set of tools for Copilot or any MCP-compatible agent—no manual endpoint wiring required.
- Combine dynamic tool generation (from OpenAPI specs) with manual overrides for full, reliable coverage.
- Build, test, and extend your own agent-ready MCP server for any API, accelerating AI-driven workflows and integrations.

**Protocol:** Implements the MCP stdio protocol (JSON-based, similar to JSON-RPC) for maximum compatibility with AI assistants and agent frameworks.

> **Note:** The automatic tool generation and auto-registered endpoints in this template are tailored for Render's OpenAPI and client structure. If you want to use this approach for a different API, you may need to write a new script or refactor the logic to match your API's format and client modules.

## Features

- Exposes nearly all Render API endpoints as MCP tools (auto-generated and manually registered for full coverage)
- Supports listing, creating, and deleting services and databases, managing deploys, environment variables, and more
- Implements robust HTTP status handling (all 2xx codes treated as success)
- Runs as a stdio MCP server (communicates over standard input/output)

## Requirements

- Python 3.10+
- [Render.com account](https://render.com/)
- Render API key (see below)
- `pip install -r requirements.txt`

## Configuration

1. Copy your Render API key from the Render dashboard.
2. Create a `.env` file in the project root:

   ```env
   RENDER_API_KEY=your_render_api_key_here
   ```

3. (Optional) Adjust any other environment variables as needed.

## Usage

You can run the MCP server directly or configure it for use with Copilot or other MCP clients.

### Direct Run

```sh
python fast-mcp/my_fastmcp_server.py
```

### VS Code Copilot MCP Integration

Add the following to your `.vscode/mcp.json`:

```jsonc
{
  "servers": {
    "my-fastmcp": {
      "command": "python",
      "args": ["fast-mcp/my_fastmcp_server.py"]
    }
  }
}
```

Then select "my-fastmcp" as your Copilot MCP server.


## Available MCP Tools

| Tool Name                                      | Description                                                                                   |
|------------------------------------------------|-----------------------------------------------------------------------------------------------|
| echo                                           | Echoes back the input text.                                                                   |
| get_render_services                            | List all Render services in your account.                                                     |
| get_render_services_service_id                  | Get a specific Render service by ID.                                                          |
| get_render_services_service_id_custom_domains   | List custom domains for a service.                                                            |
| get_render_services_service_id_deploys          | List deploys for a service.                                                                   |
| get_render_services_service_id_env_vars         | List environment variables for a service.                                                     |
| post_render_services                           | Create a new Render service.                                                                  |
| get_render_deploys_deploy_id                   | Get a specific deploy by ID.                                                                  |
| get_render_databases                           | List all database services.                                                                   |
| get_render_databases_database_id                | Get a specific database service by ID.                                                        |
| delete_render_database                         | Delete a specific database service by ID.                                                     |
| get_render_services_service_id_deploys_generated| List deploys for a service using the generated Render API client.                             |
| mcp_health                                     | MCP health check endpoint.                                                                    |
| mcp_context                                    | MCP context endpoint (stub).                                                                  |
| mcp_search                                     | MCP search endpoint (stub).                                                                   |
| post_render_create_db                          | Create a new PostgreSQL database on Render.                                                   |
| get_render_databases_database_id_connection     | Get connection info for a database.                                                           |
| get_render_databases_database_id_users          | List users for a database.                                                                    |
| retrieve_blueprint                             | Auto-generated tool to retrieve a blueprint by ID.                                         |
| retrieve_disk                                  | Auto-generated tool to retrieve a disk by ID.                                              |
| retrieve_service                               | Auto-generated tool to retrieve a service by ID.                                           |
| update_blueprint                               | Auto-generated tool to update a blueprint.                                                 |
| update_disk                                    | Auto-generated tool to update a disk.                                                      |
| update_service                                 | Auto-generated tool to update a service.                                                   |
| add_disk                                      | Auto-generated tool to add a disk.                                                          |
| create_service                                | Auto-generated tool to create a service.                                                     |
| delete_disk                                   | Auto-generated tool to delete a disk.                                                        |
| delete_service                                | Auto-generated tool to delete a service.                                                     |
| disconnect_blueprint                          | Auto-generated tool to disconnect a blueprint.                                               |
| get_user                                      | Auto-generated tool to get user information.                                                 |
> Note: Additional auto-generated tools may be available depending on the Render OpenAPI spec and client modules present.

## How it Works


### Internal Logic

- The server uses the official `openapi.yaml` from the Render API to understand all available endpoints and their parameters.
- A script parses the OpenAPI spec and generates a list of endpoints (`render_api_routes.py`).
- For each endpoint, the server attempts to dynamically register an MCP tool by importing the corresponding client module and exposing its logic as a tool.
- If an endpoint cannot be auto-generated (e.g., missing client module), a manual MCP tool is implemented to ensure full API coverage.
- All HTTP requests treat any 2xx status code as success, and handle response bodies appropriately (including 204 No Content).
- The server runs as a stdio MCP server, communicating over standard input/output, making it compatible with GitHub Copilot and other MCP clients.

### VS Code MCP Configuration

To use this server with Copilot or other MCP clients, create a `.vscode` folder in your repo (if it doesn't exist) and add a `mcp.json` file like this:

```jsonc
{
  "servers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "my-fastmcp": {
      "command": "python",
      "args": ["fast-mcp/my_fastmcp_server.py"]
    }
  }
}
```

Then select "my-fastmcp" as your Copilot MCP server in VS Code.

**Important:** The `fast-mcp` folder (containing `my_fastmcp_server.py` and related files) must be at the root of your workspace for this configuration to work with Copilot MCP. If you move or rename the folder, update the `args` path in your `mcp.json` accordingly.

## Extending

To add new endpoints or custom logic, edit `my_fastmcp_server.py` and register new MCP tools as needed.


## Acknowledgments

This project uses the official Render.com OpenAPI specification to generate MCP tools. Render and the Render logo are trademarks of Render.com.

## License

MIT
