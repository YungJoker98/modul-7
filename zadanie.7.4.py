import random

class Media:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Movie(Media):
    pass

class Series(Media):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

library = []

def get_movies():
    return sorted([media for media in library if isinstance(media, Movie)], key=lambda x: x.title)

def get_series():
    return sorted([media for media in library if isinstance(media, Series)], key=lambda x: x.title)

def search(title):
    return next((media for media in library if media.title.lower() == title.lower()), None)

def generate_views():
    media = random.choice(library)
    media.views += random.randint(1, 100)

def generate_multiple_views(times=10):
    for _ in range(times):
        generate_views()

def top_titles(n, content_type=None):
    filtered_library = library
    if content_type == "movie":
        filtered_library = get_movies()
    elif content_type == "series":
        filtered_library = get_series()
    return sorted(filtered_library, key=lambda x: x.views, reverse=True)[:n]

# Testowe dodanie danych
titles = [
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("Inception", 2010, "Sci-Fi"),
    Series("The Simpsons", 1989, "Animation", 1, 5),
    Series("Breaking Bad", 2008, "Drama", 1, 1)
]

library.extend(titles)

# Generowanie losowych odtworzeń
generate_multiple_views()

# Wyświetlanie najpopularniejszych tytułów
print("Najpopularniejsze tytuły:")
for title in top_titles(3):
    print(f"{title} - {title.views} wyświetleń")
