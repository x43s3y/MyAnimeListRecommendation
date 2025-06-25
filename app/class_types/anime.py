from typing import Optional
from class_types import genres
from pydantic import BaseModel

class Anime(BaseModel):
    title: str
    mean: float
    genre_list: list[genres.Genre]
    icon: Optional[str] = None

    def __repr__(self):
        return f"Anime({self.title} - {self.mean} - {self.genre_list})"