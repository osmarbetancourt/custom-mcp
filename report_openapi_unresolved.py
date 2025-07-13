import json
import sys
from typing import Any, Set, List

# Usage: python report_openapi_unresolved.py open-api-render.json

def collect_unresolved_refs(obj: Any, known_schemas: Set[str], known_params: Set[str], known_responses: Set[str], known_headers: Set[str], report: List[str], path="root"):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                if v.startswith("#/components/schemas/"):
                    ref_name = v.split("/")[-1]
                    if ref_name not in known_schemas:
                        report.append(f"Missing schema: {ref_name} at {path}")
                elif v.startswith("#/components/parameters/"):
                    param_name = v.split("/")[-1]
                    if param_name not in known_params:
                        report.append(f"Missing parameter: {param_name} at {path}")
                elif v.startswith("#/components/responses/"):
                    resp_name = v.split("/")[-1]
                    if resp_name not in known_responses:
                        report.append(f"Missing response: {resp_name} at {path}")
                elif v.startswith("#/components/headers/"):
                    header_name = v.split("/")[-1]
                    if header_name not in known_headers:
                        report.append(f"Missing header: {header_name} at {path}")
                else:
                    report.append(f"Unknown $ref: {v} at {path}")
            else:
                collect_unresolved_refs(v, known_schemas, known_params, known_responses, known_headers, report, path=f"{path}.{k}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            collect_unresolved_refs(item, known_schemas, known_params, known_responses, known_headers, report, path=f"{path}[{idx}]")

def main():
    if len(sys.argv) != 2:
        print("Usage: python report_openapi_unresolved.py open-api-render.json")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        openapi = json.load(f)
    schemas = set(openapi.get("components", {}).get("schemas", {}).keys())
    params = set(openapi.get("components", {}).get("parameters", {}).keys())
    responses = set(openapi.get("components", {}).get("responses", {}).keys())
    headers = set(openapi.get("components", {}).get("headers", {}).keys())
    report = []
    collect_unresolved_refs(openapi, schemas, params, responses, headers, report)
    if report:
        print("Unresolved references found:")
        for r in report:
            print(f"  - {r}")
    else:
        print("No unresolved references found.")

if __name__ == "__main__":
    main()
