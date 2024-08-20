import http
import json
import requests

# def get_lyrics(artist, title):
#     URL = f"https://api.lyrics.ovh/v1/{artist}/{title}"
#     response = requests.get(url=URL)
#     data = response.json()
#     if 'lyrics' not in data:
#         return "Lyrics not found"
#     return data['lyrics'] 

def get_lyrics(song):
    conn = http.client.HTTPSConnection("saavn.dev")

    conn.request("GET", "/api/search/songs?query="+song)

    res = conn.getresponse()
    data = res.read()

    data_dict = json.loads(data.decode("utf-8"))


    with open(f"song.json", "w", encoding="utf-8") as file:
        json.dump(data_dict, file, ensure_ascii=False, indent=4)