import requests
import sys

API_URL = "http://localhost:9000/ask/render"


def create_db_on_render(db_name, region="oregon"):
    url = "http://localhost:9000/render/create-db"
    payload = {"name": db_name, "region": region}
    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        print(f"MCP: Database '{data.get('name')}' created! Dashboard: {data.get('dashboardUrl')} Status: {data.get('status')}\n")
    except Exception as e:
        print(f"[Error creating DB] {e}\n")

import re
def ask_mcp(question):
    # Simple intent recognition for DB creation
    match = re.search(r"create (?:a|an)? ?(?:free )?(?:tier )?db (?:on|in)? render.*call (?:it|him|her|them)? ['\"]?([\w-]+)['\"]?", question, re.IGNORECASE)
    if match:
        db_name = match.group(1)
        create_db_on_render(db_name)
        return
    # Default: send to LLM
    try:
        resp = requests.post(API_URL, json={"question": question})
        resp.raise_for_status()
        answer = resp.json().get("answer", "[No answer returned]")
        print(f"MCP: {answer}\n")
    except Exception as e:
        print(f"[Error] {e}\n")

def main():
    if len(sys.argv) > 1:
        # Non-interactive: use command-line argument as question
        question = " ".join(sys.argv[1:])
        ask_mcp(question)
        return
    print("MCP Render Q&A Bridge\nType your question about your Render.com services (or 'exit' to quit):\n")
    while True:
        question = input("You: ")
        if question.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        ask_mcp(question)

if __name__ == "__main__":
    main()
