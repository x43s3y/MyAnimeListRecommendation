from app import utils


def user_anime_refinement(response, excluded_status: list):
    raw_anime_data = response.json()["data"]
    all_animes = utils.defining_animes(raw_anime_data)
    return all_animes