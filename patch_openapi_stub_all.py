import json
import sys
from typing import Any, Dict, Set, List

# Usage: python patch_openapi_stub_all.py open-api-render.json

def find_missing_refs(obj: Any, known_defs: Set[str], missing: Set[str], missing_params: Set[str], known_params: Set[str], missing_props: List[str]):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                if v.startswith("#/components/schemas/"):
                    ref_name = v.split("/")[-1]
                    if ref_name not in known_defs:
                        missing.add(ref_name)
                elif v.startswith("#/components/parameters/"):
                    param_name = v.split("/")[-1]
                    if param_name not in known_params:
                        missing_params.add(param_name)
            elif k == "properties" and isinstance(v, dict):
                for prop, prop_val in v.items():
                    if "$ref" in prop_val:
                        ref = prop_val["$ref"]
                        if ref.startswith("#/components/schemas/"):
                            ref_name = ref.split("/")[-1]
                            if ref_name not in known_defs:
                                missing.add(ref_name)
                        elif ref.startswith("#/components/parameters/"):
                            param_name = ref.split("/")[-1]
                            if param_name not in known_params:
                                missing_params.add(param_name)
                    # Check for missing nested properties
                    if isinstance(prop_val, dict) and "properties" in prop_val:
                        for nested_prop in prop_val["properties"]:
                            if not isinstance(prop_val["properties"], dict) or nested_prop not in prop_val["properties"]:
                                missing_props.append(f"{prop}.{nested_prop}")
            else:
                find_missing_refs(v, known_defs, missing, missing_params, known_params, missing_props)
    elif isinstance(obj, list):
        for item in obj:
            find_missing_refs(item, known_defs, missing, missing_params, known_params, missing_props)

def patch_openapi_with_stubs(openapi: Dict[str, Any], missing: Set[str], missing_params: Set[str], missing_props: List[str]):
    schemas = openapi.setdefault("components", {}).setdefault("schemas", {})
    for name in missing:
        if name not in schemas:
            schemas[name] = {
                "type": "object",
                "description": f"Stub for missing schema: {name}",
                "properties": {},
            }
    params = openapi.setdefault("components", {}).setdefault("parameters", {})
    for pname in missing_params:
        if pname not in params:
            params[pname] = {
                "name": pname,
                "in": "query",
                "schema": {"type": "string"},
                "description": f"Stub for missing parameter: {pname}",
                "required": False
            }
    # Note: missing_props is just for reporting, not patched automatically (needs manual review)

def main():
    if len(sys.argv) != 2:
        print("Usage: python patch_openapi_stub_all.py open-api-render.json")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        openapi = json.load(f)
    schemas = openapi.get("components", {}).get("schemas", {})
    params = openapi.get("components", {}).get("parameters", {})
    known_defs = set(schemas.keys())
    known_params = set(params.keys())
    missing = set()
    missing_params = set()
    missing_props = []
    find_missing_refs(openapi, known_defs, missing, missing_params, known_params, missing_props)
    missing = missing - known_defs
    missing_params = missing_params - known_params
    if not missing and not missing_params:
        print("No missing schemas or parameters detected.")
    else:
        print(f"Stubbing {len(missing)} missing schemas: {sorted(missing)}")
        print(f"Stubbing {len(missing_params)} missing parameters: {sorted(missing_params)}")
        patch_openapi_with_stubs(openapi, missing, missing_params, missing_props)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(openapi, f, indent=2)
        print(f"Patched {path} with stubs for missing schemas and parameters.")
    if missing_props:
        print("Potential missing nested properties (manual review suggested):")
        for p in missing_props:
            print(f"  - {p}")
    else:
        print("No missing nested properties detected.")

if __name__ == "__main__":
    main()
