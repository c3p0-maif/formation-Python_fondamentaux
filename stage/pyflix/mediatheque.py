class Episode:
    def __init__(self, title: str, number: int, season_number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = int(number)
        self.season_number = int(season_number)
        self.duration = int(duration) if duration is not None else None
        self.year = int(year) if year else None

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.number, self.season_number) == (other.number, other.season_number)

    def __str__(self):
        return f"Épisode {self.title} [{self.season_number:02}x{self.number:02}]"

    def __repr__(self):
        return f"Episode('{self.title}', {self.number}, {self.season_number}, {self.duration}, {self.year})"


class TvShow:
    def __init__(self, name: str):
        self.name = name.title()
        self._episodes = []

    def add_episode(self, title: str, number: int, season_number: int,
                    duration: int, year: int):
        ep = Episode(title, number, season_number,
                     duration, year)
        if ep in self._episodes:
            raise ValueError(f"Episode déjà présent {ep}")
        self._episodes.append(ep)

    @property
    def episodes(self):
        return self._episodes.copy()

