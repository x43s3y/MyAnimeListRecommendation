# MyAnimeListRecommendation
Website where you are able to find good anime through myanimelist account

---

## Approach MyAnimeList **API**
1. Get needed information
- get user's MAL nickname
- get desired __**score**__ to be filtered by
- get desired __**date**__ to be filtered by
2. get users animes by nickname
- use the nickname as the endpoint pointer to the user's anime list

---

## Response handling
1. Check the response validation
- remove EMPTY
- filter by criterea 