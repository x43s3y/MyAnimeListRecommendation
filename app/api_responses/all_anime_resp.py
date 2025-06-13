from app.class_types.anime import Anime
from app.class_types.genres import Genre

def all_anime_refinement(response):
    all_animes = defining_animes(response.json()["data"])
    animes_on_genres = sorting_on_genre(all_animes)
    return animes_on_genres

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