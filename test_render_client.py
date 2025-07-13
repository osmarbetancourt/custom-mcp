
import os
from dotenv import load_dotenv
from render_public_api_client.client import Client
from render_public_api_client.api.services import list_services

# Load .env file
load_dotenv()
token = os.getenv("RENDER_API_KEY")

if not token:
    raise RuntimeError("RENDER_API_KEY not found in environment.")

client = Client(base_url="https://api.render.com/v1", headers={"Authorization": f"Bearer {token}"})

def test_get_endpoints():
    print("Testing GET /services (list_services)...")
    try:
        response = list_services.sync(client=client)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_get_endpoints()
