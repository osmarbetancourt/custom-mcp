from fastmcp import FastMCP
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
import importlib
from render_api_routes import render_api_routes

RENDER_API_URL = "https://api.render.com/v1"
RENDER_API_KEY = os.getenv("RENDER_API_KEY")


# Create the MCP server instance
def main():
    mcp = FastMCP(name="My FastMCP Server")

    print("[MCP SERVER] Starting My FastMCP Server...")

    @mcp.tool
    def echo(text: str) -> str:
        """Echoes back the input text."""
        return text

    # Dynamically register all Render API endpoints as MCP tools
    import inspect
    registered_tools = 0
    for entry in render_api_routes:
        route = entry["route"]
        op_id = entry["operationId"]
        parts = route.strip('/').split('/')
        module_parts = [p for p in parts if not (p.startswith('{') and p.endswith('}'))]
        module_path = f"render_public_api_client.api.{'.'.join(module_parts)}.{op_id}"
        try:
            api_module = importlib.import_module(module_path)
            func = getattr(api_module, "sync")
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"[MCP TOOL SKIP] {module_path}: {e}")
            continue

        sig = inspect.signature(func)
        # Exclude 'client' param
        params = [p for p in sig.parameters.values() if p.name != 'client']
        param_strs = []
        call_args = []
        for p in params:
            if p.default is inspect.Parameter.empty:
                param_strs.append(f"{p.name}")
            else:
                param_strs.append(f"{p.name}={repr(p.default)}")
            call_args.append(f"{p.name}={p.name}")
        param_sig = ", ".join(param_strs)
        call_sig = ", ".join(call_args)
        func_code = f"""
def tool_func({param_sig}):
    from render_public_api_client.client import AuthenticatedClient
    import os
    api_key = os.getenv('RENDER_API_KEY')
    if not api_key:
        raise Exception('RENDER_API_KEY not set in environment')
    client = AuthenticatedClient(base_url='https://api.render.com/v1', token=api_key)
    return func(client=client{', ' if call_sig else ''}{call_sig})
"""
        local_vars = {'func': func}
        try:
            exec(func_code, local_vars)
            tool = local_vars['tool_func']
            tool.__name__ = op_id
            tool.__doc__ = f"Auto-generated tool for {op_id}"
            mcp.tool(tool)
            registered_tools += 1
        except Exception as e:
            print(f"[MCP TOOL SKIP] {op_id}: error creating tool: {e}")
            continue

    print(f"[MCP SERVER] Registered {registered_tools} auto-generated Render API tools.")

    @mcp.tool
    def post_render_services_service_id_deploys(service_id: str, body: dict = None) -> dict:
        """
        Trigger a deploy for the service with the provided ID.
        body can include: clearCache (str), commitId (str), imageUrl (str)
        """
        url = f"{RENDER_API_URL}/services/{service_id}/deploys"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.post(url, headers=headers, json=body or {})
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()
        
    @mcp.tool
    def get_render_services() -> list:
        """List all Render services in your account. Requires your Render API key as input."""
        url = RENDER_API_URL+"/services"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_services_service_id(service_id: str) -> dict:
        """Get a specific Render service."""
        url = f"{RENDER_API_URL}/services/{service_id}"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_services_service_id_custom_domains(service_id: str) -> dict:
        """List custom domains for a service."""
        url = f"{RENDER_API_URL}/services/{service_id}/custom-domains"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_services_service_id_deploys(service_id: str) -> dict:
        """List deploys for a service."""
        url = f"{RENDER_API_URL}/services/{service_id}/deploys"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_services_service_id_env_vars(service_id: str) -> dict:
        """List environment variables for a service."""
        url = f"{RENDER_API_URL}/services/{service_id}/env-vars"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def post_render_services(body: dict) -> dict:
        """Create a new Render service."""
        url = f"{RENDER_API_URL}/services"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.post(url, headers=headers, json=body)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_deploys_deploy_id(deploy_id: str) -> dict:
        """Get a specific deploy."""
        url = f"{RENDER_API_URL}/deploys/{deploy_id}"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_databases() -> list:
        """List all database services."""
        url = f"{RENDER_API_URL}/postgres"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        data = resp.json()
        if not isinstance(data, list):
            return []
        return data

    @mcp.tool
    def get_render_databases_database_id(database_id: str) -> dict:
        """Get a specific database service."""
        url = f"{RENDER_API_URL}/postgres/{database_id}"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def delete_render_database(database_id: str) -> dict:
        """Delete a specific database service."""
        url = f"{RENDER_API_URL}/postgres/{database_id}"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.delete(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return {"detail": "Database deleted"}

    @mcp.tool
    def get_render_services_service_id_deploys_generated(service_id: str, limit: int = 20) -> list:
        """List deploys for a service using the generated Render API client."""
        from render_public_api_client.api.deploys import list_deploys
        from render_public_api_client.client import AuthenticatedClient
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        client = AuthenticatedClient(base_url=RENDER_API_URL, token=api_key)
        result = list_deploys.sync(service_id=service_id, client=client, limit=limit)
        if isinstance(result, list):
            return [d.to_dict() for d in result]
        else:
            raise Exception(f"Render API error: {result}")

    @mcp.tool
    def mcp_health() -> dict:
        """MCP health check endpoint."""
        return {"status": "ok"}

    @mcp.tool
    def mcp_context(request: dict) -> dict:
        """MCP context endpoint (stub)."""
        return {"context": [], "request": request}

    @mcp.tool
    def mcp_search(request: dict) -> dict:
        """MCP search endpoint (stub)."""
        return {"results": [], "request": request}

    @mcp.tool
    def post_render_create_db(body: dict) -> dict:
        """Create a new PostgreSQL database on Render."""
        url = f"{RENDER_API_URL}/postgres"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.post(url, headers=headers, json=body)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_databases_database_id_connection(database_id: str) -> dict:
        """Get connection info for a database."""
        url = f"{RENDER_API_URL}/postgres/{database_id}/connection"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    @mcp.tool
    def get_render_databases_database_id_users(database_id: str) -> dict:
        """List users for a database."""
        url = f"{RENDER_API_URL}/postgres/{database_id}/users"
        api_key = os.getenv("RENDER_API_KEY")
        if not api_key:
            raise Exception("RENDER_API_KEY not set in environment")
        headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
        resp = httpx.get(url, headers=headers)
        if not (200 <= resp.status_code < 300):
            raise Exception(f"Render API error: {resp.status_code} {resp.text}")
        return resp.json()

    if __name__ == "__main__":
        mcp.run()

main()
