# orchestrator.py
"""
Main orchestration script for MCP:
- Loads config
- For each enabled provider, downloads/updates docs from GitHub repos/URLs
- Stores docs in local folder
- Chunks, deduplicates, and embeds new/changed content into vector DB
- Logs/report status for each provider
"""


import os
import subprocess
from pathlib import Path
from config_loader import load_config
from dotenv import load_dotenv


# Load .env for MCP_DATA_ROOT
load_dotenv()
MCP_DATA_ROOT = os.getenv("MCP_DATA_ROOT", str(Path.home() / "mcp_data"))

    return Path(MCP_DATA_ROOT) / project_name / "external_docs"

    pass  # Repo syncing removed

    pass  # Chunking removed

    name = provider["name"]
    print(f"\n=== Processing provider: {name} ===")
    print(f"[INFO] (Repo syncing, chunking, and embedding skipped for {name}.)")

    config = load_config()
    project_name = config["project"]["name"]
    docs_root = get_docs_root(project_name)
    docs_root.mkdir(parents=True, exist_ok=True)
    for provider in config["providers"]:
        if provider.get("enabled", False):
            process_provider(provider, docs_root)
    print(f"\nAll providers processed. (Repo syncing, chunking, and embedding skipped. MCP is ready for web-based RAG or Copilot search.)")

if __name__ == "__main__":
    main()
