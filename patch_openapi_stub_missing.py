import json
import sys
from typing import Any, Dict, Set

# Usage: python patch_openapi_stub_missing.py open-api-render.json

def find_missing_refs(obj: Any, known_defs: Set[str], missing: Set[str]):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                if v.startswith("#/components/schemas/"):
                    ref_name = v.split("/")[-1]
                    if ref_name not in known_defs:
                        missing.add(ref_name)
            else:
                find_missing_refs(v, known_defs, missing)
    elif isinstance(obj, list):
        for item in obj:
            find_missing_refs(item, known_defs, missing)

def patch_openapi_with_stubs(openapi: Dict[str, Any], missing: Set[str]):
    schemas = openapi.setdefault("components", {}).setdefault("schemas", {})
    for name in missing:
        if name not in schemas:
            schemas[name] = {
                "type": "object",
                "description": f"Stub for missing schema: {name}",
                "properties": {},
            }

def main():
    if len(sys.argv) != 2:
        print("Usage: python patch_openapi_stub_missing.py open-api-render.json")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        openapi = json.load(f)
    schemas = openapi.get("components", {}).get("schemas", {})
    known_defs = set(schemas.keys())
    missing = set()
    find_missing_refs(openapi, known_defs, missing)
    missing = missing - known_defs
    if not missing:
        print("No missing schemas detected.")
        return
    print(f"Stubbing {len(missing)} missing schemas: {sorted(missing)}")
    patch_openapi_with_stubs(openapi, missing)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(openapi, f, indent=2)
    print(f"Patched {path} with stubs for missing schemas.")

if __name__ == "__main__":
    main()
