from class_types import genres

class Anime():
    def __init__(self, title: str, mean: float, genre_list: list[genres.Genre]):
        self._title = title
        self._mean = mean
        self._genres = genre_list

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def mean(self):
        return self._mean
    @mean.setter
    def mean(self, value):
        if value is float:
            self._mean = value
        else:
            raise ValueError("Mean is supposed to be a float number")
    
    @property
    def genres(self):
        return self._genres
    @genres.setter
    def genres(self, value):
        if value is list:
            self._genres = value
        else:
            raise ValueError("Genres are supposed to be a list")

    def __repr__(self):
        return f"Anime({self.title} - {self.mean} - {self.genres})"