from typing import Annotated
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from dotenv import load_dotenv
from api_responses.user_resp import user_anime_refinement
from api_responses.all_anime_resp import all_anime_refinement, sorting_on_genre
import httpx
import os

app = FastAPI()
load_dotenv(dotenv_path="../authentication/.env")

origin = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID:
    raise RuntimeError("CLIENT_ID is not set in the environment variables")

if not CLIENT_SECRET:
    raise RuntimeError("CLIENT_SECRET is not set in environment variables")

API_ENDPOINT = "https://api.myanimelist.net/v2/"
user = "simeon02" #CHANGE TO INPUT FROM FE
#TODO: my_list_status aint working check postman
ALL_ANIME_ENDPOINT = f"{API_ENDPOINT}anime/ranking?ranking_type=all&limit=500&fields=mean,genres,my_list_status"
USER_ANIME_ENDPOINT = f"{API_ENDPOINT}users/{user}/animelist?fields=list_status,mean,genres&nsfw=true&limit=1000"

headers = {
    'X-MAL-CLIENT-ID': CLIENT_ID
}

all_animes = []
animes_on_genres = {}

@app.get("/all-anime")
async def all_anime_resp():
    async with httpx.AsyncClient() as client:
        response = await client.get(ALL_ANIME_ENDPOINT, headers=headers)
        response.raise_for_status()
        return all_anime_refinement(response)

@app.get("/user-anime-genres")
async def user_genres_resp():
    async with httpx.AsyncClient() as client:
        response = await client.get(ALL_ANIME_ENDPOINT, headers=headers)
        response.raise_for_status()
        return sorting_on_genre(response)
    
@app.get("/user-anime")
async def user_anime_resp():
    async with httpx.AsyncClient() as client:
        response = await client.get(USER_ANIME_ENDPOINT, headers=headers)
        response.raise_for_status()
        excluded_status = []
        return user_anime_refinement(response, excluded_status)
        

