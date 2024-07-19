import requests

def get_lyrics(artist, title):
    URL = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url=URL)
    data = response.json()
    return data["lyrics"]