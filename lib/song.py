class Song:

    count = 0
    genres = []
    artists = []
    artist_count = {}
    genre_count = {}
    
    def __init__(self, name:str, artist:str, genre:str) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(self.artist)
        Song.genres.append(self.genre)

        if Song.artist_count.get(f"{self.artist}") == None:
            Song.artist_count[f"{self.artist}"] = 1
        elif Song.artist_count.get(f"{self.artist}") != None:
            Song.artist_count[f"{self.artist}"] += 1

        if Song.genre_count.get(f"{self.genre}") == None:
            Song.genre_count[f"{self.genre}"] = 1
        elif Song.genre_count.get(f"{self.genre}") != None:
            Song.genre_count[f"{self.genre}"] += 1

    