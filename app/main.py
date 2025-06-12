from typing import Annotated
from fastapi import FastAPI, Header
from dotenv import load_dotenv
from class_types import anime
from class_types import genres
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

ALL_ANIME_ENDPOINT = f"{API_ENDPOINT}anime/ranking?ranking_type=all&limit=500&fields=mean,genres"
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

def defining_animes(animes: list) -> list[anime.Anime]:
    response = []
    for resp in animes:
            anime_data = resp["node"]
            anime_title = anime_data["title"]
            anime_mean = anime_data["mean"]
            anime_genres = assign_to_genre(anime_data["genres"])
            response.append(anime.Anime(anime_title, anime_mean, anime_genres))
    return response

def assign_to_genre(genres_list: list) -> list[genres.Genre]:
    assigned_list = []
    for genre in genres_list:
        print(genre)
        assigned_list.append(genres.Genre(genre["id"], genre["name"]))

    return assigned_list

def sorting_on_genre(animes: list[anime.Anime]) -> dict[genres.Genre.genre, anime.Anime.title]:
    genres = {}
    for anime in animes:
        for genre in anime.genres:
            if genre.genre not in genres:
                genres[genre.genre] = f"{anime.title}, " 
            genres[genre.genre] += f"{anime.title}, " 
    return genres