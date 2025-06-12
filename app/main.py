from typing import Annotated
from fastapi import FastAPI, Header
from dotenv import load_dotenv
from class_types.anime import Anime
from class_types.genres import Genre
from api_responses.user_resp import user_anime_refinment
import httpx
import os

app = FastAPI()
load_dotenv(dotenv_path="../authentication/.env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID:
    raise RuntimeError("CLIENT_ID is not set in the environment variables")

if not CLIENT_SECRET:
    raise RuntimeError("CLIENT_SECRET is not set in environment variables")

API_ENDPOINT = "https://api.myanimelist.net/v2/"
user = "x43s3y" #CHANGE TO INPUT FROM FE
ALL_ANIME_ENDPOINT = f"{API_ENDPOINT}anime/ranking?ranking_type=all&limit=500&fields=mean,genres"
USER_ANIME_ENDPOINT = f"{API_ENDPOINT}users/{user}/animelist?fields=list_status&nsfw=true&limit=1000"

headers = {
    'X-MAL-CLIENT-ID': CLIENT_ID
}

all_animes = []
animes_on_genres = {}

@app.get("/")
async def all_anime_resp():
    async with httpx.AsyncClient() as client:
        response = await client.get(ALL_ANIME_ENDPOINT, headers=headers)
        response.raise_for_status()
        all_animes = defining_animes(response.json()["data"])
        animes_on_genres = sorting_on_genre(all_animes)
        return animes_on_genres
    # DO THE SAME AS USER TO SORT CODE IN DIFFERNET MODULE
    
@app.get("/user")
async def user_anime_resp():
    async with httpx.AsyncClient() as client:
        response = await client.get(USER_ANIME_ENDPOINT, headers=headers)
        response.raise_for_status()
        excluded_status = []
        return user_anime_refinment(response, excluded_status)
        

def defining_animes(animes: list) -> list[Anime]:
    response = []
    for resp in animes:
            anime_data = resp["node"]
            anime_title = anime_data["title"]
            anime_mean = anime_data["mean"]
            anime_genres = assign_anime_to_genre(anime_data["genres"])
            response.append(Anime(anime_title, anime_mean, anime_genres))
    return response

def assign_anime_to_genre(genres_list: list) -> list[Genre]:
    assigned_list = []
    for genre in genres_list:
        assigned_list.append(Genre(genre["id"], genre["name"]))

    return assigned_list

def sorting_on_genre(animes: list[Anime]) -> dict[Genre.genre, Anime.title]:
    genres = {}
    for anime in animes:
        for genre in anime.genres:
            if genre.genre not in genres:
                genres[genre.genre] = f"{anime.title}, " 
            genres[genre.genre] += f"{anime.title}, " 
    return genres

