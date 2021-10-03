import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import youtube_dl
youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"


class Song(object):
    def __init__(self, artist, song_name):
        self.artist = artist
        self.song_name = song_name


class Playlist(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title


class YouTubeClient(object):
    def __init__(self, client_credentials_file):

        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_credentials_file, scopes)
        credentials = flow.run_console()

        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        self.youtube_client = youtube_client

    def youtube_get_all_playlists(self):
        request = self.youtube_client.playlists().list(
            part="id, snippet",
            mine=True
        )
        response = request.execute()
        all_playlists = []

        for playlist in response['items']:
            all_playlists.append(Playlist(playlist['id'], playlist['snippet']['title']))

        return all_playlists

    def youtube_songs_in_playlist(self, playlist_id):
        songs = []
        request = self.youtube_client.playlistItems().list(
            playlistId=playlist_id,
            part="id, snippet"
        )
        response = request.execute()

        for song in response['items']:
            video_id = song['snippet']['resourceId']['videoId']
            artist, song_name = self.youtube_get_artist_and_songname(video_id)

            if artist and song_name:
                songs.append(Song(artist, song_name))

        return songs

    def youtube_get_artist_and_songname(self, video_id):
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        video = youtube_dl.YoutubeDL({}).extract_info(
            youtube_url, download=False)

        artist = video["artist"]
        song_name = video["track"]

        return artist, song_name
