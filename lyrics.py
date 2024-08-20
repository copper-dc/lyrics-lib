import http
import json
import requests


def get_lyrics_by_song_name(song_name):
    conn = http.client.HTTPSConnection("saavn.dev")
    conn.request("GET", f"/api/search/songs?query={song_name}")
    
    res = conn.getresponse()
    data = res.read()

    
    search_data = json.loads(data.decode("utf-8"))

    if search_data['success']:
        song_id = search_data['data']['results'][0]['id']
        print(f"Found song: {search_data['data']['results'][0]['name']}, ID: {song_id}")

        conn.request("GET", f"/api/songs/{song_id}/lyrics")
        res = conn.getresponse()
        lyrics_data = res.read()

        lyrics_data = json.loads(lyrics_data.decode("utf-8"))

        if lyrics_data['success']:
            lyrics = lyrics_data['data']['lyrics']
            print(f"Lyrics: {lyrics}")
            return lyrics
        else:
            print("Lyrics not found")
    else:
        print("Song not found")