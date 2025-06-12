def user_anime_refinment(response, excluded_status: list):
    resp = []
    for anime in response.json()["data"]:
        if anime["list_status"]["status"] not in excluded_status:
            resp.append(anime)
    return resp