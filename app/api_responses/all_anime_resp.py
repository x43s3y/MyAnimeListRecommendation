from app import utils
from app.class_types.anime import Anime
from app.class_types.genres import Genre

def all_anime_refinement(response):
    all_animes = utils.defining_animes(response.json()["data"])
    return all_animes


def sorting_on_genre(response):
    animes = utils.defining_animes(response.json()["data"])
    genres = {}
    for anime in animes:
        for genre in anime.genre_list:
            if genre.genre not in genres:
                genres[genre.genre] = 1 
            genres[genre.genre] += 1 
    return genres