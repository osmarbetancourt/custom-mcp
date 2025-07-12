from fastapi import FastAPI
from app.api import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Custom MCP Server is running."}
