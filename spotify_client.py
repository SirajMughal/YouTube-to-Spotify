import requests
import urllib.parse


class SpotifyClient(object):

    def __init__(self, spotify_api_token):
        self.spotify_api_token = spotify_api_token

    def spotify_song_search(self, artist, song_name):
        query = urllib.parse.quote(f'{artist} {song_name}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_api_token}"
            }
        )
        json_response = response.json()
        results = json_response["tracks"]["items"]

        if results:
            return results[0]['id']

    def spotify_add_song(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"

        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_api_token}"
            }
        )
        return response.ok
