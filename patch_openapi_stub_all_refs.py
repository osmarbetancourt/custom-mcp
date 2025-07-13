import json
import sys
from typing import Any, Dict, Set
import re

# Usage: python patch_openapi_stub_all_refs.py open-api-render.json

def parse_ref(ref: str):
    # Returns (section, name) or (None, None) for unknown
    m = re.match(r"#/components/(schemas|parameters|responses|headers)/([^/]+)", ref)
    if m:
        return m.group(1), m.group(2)
    # For path/inline refs, treat as schemas with safe name
    m2 = re.match(r"#/paths/(.+)", ref)
    if m2:
        # Replace non-alphanum with _
        safe = m2.group(1).replace('/', '_').replace('~1', '_').replace('%7B', '').replace('%7D', '')
        return 'schemas', f'inline_{safe}'
    return None, None

def collect_all_refs(obj: Any, found_refs: Set[str]):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                found_refs.add(v)
            else:
                collect_all_refs(v, found_refs)
    elif isinstance(obj, list):
        for item in obj:
            collect_all_refs(item, found_refs)

def patch_openapi_with_all_stubs(openapi: Dict[str, Any], refs: Set[str]):
    comps = openapi.setdefault("components", {})
    for ref in refs:
        section, name = parse_ref(ref)
        if not section or not name:
            continue
        section_dict = comps.setdefault(section, {})
        if name not in section_dict:
            # Use generic stubs for each section
            if section == "schemas":
                section_dict[name] = {"type": "object", "description": f"Stub for {ref}", "properties": {}}
            elif section == "parameters":
                section_dict[name] = {"name": name, "in": "query", "schema": {"type": "string"}, "description": f"Stub for {ref}", "required": False}
            elif section == "responses":
                section_dict[name] = {"description": f"Stub for {ref}", "content": {"application/json": {"schema": {"type": "object"}}}}
            elif section == "headers":
                section_dict[name] = {"description": f"Stub for {ref}", "schema": {"type": "string"}}

def main():
    if len(sys.argv) != 2:
        print("Usage: python patch_openapi_stub_all_refs.py open-api-render.json")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        openapi = json.load(f)
    found_refs = set()
    collect_all_refs(openapi, found_refs)
    patch_openapi_with_all_stubs(openapi, found_refs)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(openapi, f, indent=2)
    print(f"Patched {path} with stubs for all referenced components (schemas, parameters, responses, headers, and inline path refs).")

if __name__ == "__main__":
    main()
