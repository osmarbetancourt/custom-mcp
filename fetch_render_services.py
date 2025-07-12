import requests
import json
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generic MCP API caller and JSON saver.")
    parser.add_argument("endpoint", help="API endpoint, e.g. /render/services")
    parser.add_argument("-X", "--method", default="GET", help="HTTP method (GET, POST, etc.)")
    parser.add_argument("-d", "--data", default=None, help="Request body as JSON string (for POST/PUT)")
    parser.add_argument("-o", "--output", default=None, help="Output file name. If not set, will auto-generate based on endpoint.")
    parser.add_argument("--base-url", default="http://localhost:9000", help="Base URL of MCP server")
    args = parser.parse_args()


    url = args.base_url.rstrip("/") + "/" + args.endpoint.lstrip("/")
    method = args.method.upper()
    headers = {"Content-Type": "application/json"}
    data = None
    if args.data:
        try:
            data = json.loads(args.data)
        except Exception:
            print("[ERROR] Could not parse --data as JSON. Use a valid JSON string.")
            sys.exit(1)

    try:
        resp = requests.request(method, url, headers=headers, json=data)
        resp.raise_for_status()
    except Exception as e:
        print(f"[ERROR] Request failed: {e}")
        sys.exit(1)

    # Auto-generate output path if not provided
    if args.output:
        output_path = args.output
    else:
        # e.g., /render/services -> context_for_copilot/render/services.json
        endpoint_parts = args.endpoint.strip("/").split("/")
        if len(endpoint_parts) == 1:
            subfolder = endpoint_parts[0]
            filename = "response.json"
        else:
            subfolder = endpoint_parts[0]
            filename = "_".join(endpoint_parts[1:]) + ".json"
        import os
        os.makedirs(f"context_for_copilot/{subfolder}", exist_ok=True)
        output_path = f"context_for_copilot/{subfolder}/{filename}"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(resp.json(), f, indent=2)
    print(f"Saved response to {output_path}")

if __name__ == "__main__":
    main()
