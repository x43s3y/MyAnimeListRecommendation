from typing import Annotated
from fastapi import FastAPI, Header
from dotenv import load_dotenv
import httpx
import os

app = FastAPI()
load_dotenv(dotenv_path="../authentication/.env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID:
    raise RuntimeError("CLIENT_ID is not set in the environment variables")

API_ENDPOINT = "https://api.myanimelist.net/v2/anime/ranking?ranking_type=all&limit=500&fields=mean"

headers = {
    'X-MAL-CLIENT-ID': CLIENT_ID
}

@app.get("/")
async def read_root():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_ENDPOINT, headers=headers)
        response.raise_for_status()
        return response.json() 