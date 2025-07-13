# Experimental: Auto-register FastAPI routes for all render_client endpoints
# This file is for development/testing only. Do NOT use in production as-is.

import os
from fastapi import APIRouter, HTTPException, Request
from render_public_api_client.client import AuthenticatedClient
from render_public_api_client.types import UNSET
from render_api_routes import render_api_routes
import importlib

router = APIRouter()

RENDER_API_KEY = os.getenv("RENDER_API_KEY")

if not RENDER_API_KEY:
    raise RuntimeError("RENDER_API_KEY not set in environment")

client = AuthenticatedClient(
    base_url="https://api.render.com/v1",
    token=RENDER_API_KEY
)

def get_func(api_module, func_name):
    try:
        return getattr(api_module, func_name)
    except AttributeError:
        return None



for entry in render_api_routes:
    route = entry["route"]
    methods = entry["methods"]
    op_ids = entry["operationId"]
    if isinstance(op_ids, str):
        op_ids = [op_ids]
    for method, op_id in zip(methods, op_ids):
        # New logic: import module like render_public_api_client.api.services.list_services for /services GET
        parts = route.strip('/').split('/')
        # Remove path params for module path
        module_parts = [p for p in parts if not (p.startswith('{') and p.endswith('}'))]
        # Use operationId to guess the function/module name
        op_snake = op_id.replace('-', '_')
        # Try to find a module that matches the operation
        module_path = f"render_public_api_client.api.{'.'.join(module_parts)}.{op_snake}"
        print(f"[AUTO ROUTES] Trying: {method} {route} -> {module_path}.sync")
        try:
            api_module = importlib.import_module(module_path)
        except ModuleNotFoundError as e:
            print(f"[AUTO ROUTES]   Module not found: {module_path} ({e})")
            continue
        # Use 'sync' for GET, 'sync' for POST, PATCH, DELETE for now
        func = get_func(api_module, 'sync')
        if not func:
            print(f"[AUTO ROUTES]   Function not found: sync in {module_path}")
            continue
        # Define a generic endpoint
        async def endpoint(request: Request, func=func):
            try:
                result = func(client=client)
                if isinstance(result, list):
                    return [r.to_dict() for r in result]
                elif hasattr(result, 'to_dict'):
                    return result.to_dict()
                else:
                    return result
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        router.add_api_route(
            f"/auto{route}", endpoint, methods=[method]
        )
        print(f"[AUTO ROUTES]   Registered: /auto{route} [{method}]")

# To use: from render_auto_routes import router and include_router(router) in your FastAPI app
