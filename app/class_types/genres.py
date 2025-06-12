class Genre():
    def __init__(self, id: int, genre: str):
        self._id = id
        self._genre = genre

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if value is int:
            self._id = value

    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, value):
        if value is str:
            self._genre = value