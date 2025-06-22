from app import utils
from app.class_types.anime import Anime
from app.class_types.genres import Genre

def all_anime_refinement(response):
    all_animes = utils.defining_animes(response.json()["data"])
    animes_on_genres = sorting_on_genre(all_animes)
    return animes_on_genres


def sorting_on_genre(animes: list[Anime]):
    genres = {}
    print(animes)
    for anime in animes:
        for genre in anime.genres:
            if genre.genre not in genres:
                genres[genre.genre] = f"{anime.title}, " 
            genres[genre.genre] += f"{anime.title}, " 
    return genres