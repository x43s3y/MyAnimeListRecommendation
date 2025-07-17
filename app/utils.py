from app.class_types.anime import Anime
from app.class_types.genres import Genre


def defining_animes(animes: list) -> list[Anime]:
    response = []
    for resp in animes:
        anime_data = resp["node"]
        anime_title = anime_data["title"]
        anime_mean = anime_data["mean"]
        anime_picture = anime_data["main_picture"]["medium"]
        anime_genres = assign_anime_to_genre(anime_data["genres"])
        if anime_picture:
            response.append(Anime(title=anime_title, mean=anime_mean, genre_list=[g.model_dump() for g in anime_genres], icon=anime_picture))
        else:
            response.append(Anime(title=anime_title, mean=anime_mean, genre_list=[g.model_dump() for g in anime_genres]))
    return response

def assign_anime_to_genre(genres_list: list) -> list[Genre]:
    assigned_list = []
    for genre in genres_list:
        name = genre["name"]
        assigned_list.append(Genre(genre=name))

    return assigned_list