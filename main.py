from lyrics import get_lyrics

if __name__ == "__main__":
    Artist = input("Enter the artist: ")
    Song = input("Enter the song: ")
    print(get_lyrics(Artist, Song))
    