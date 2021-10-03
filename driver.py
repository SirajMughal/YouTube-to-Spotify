from spotify_client import SpotifyClient
from youtube_client import YouTubeClient
import os

import colorama
from colorama import Fore
colorama.init()


def driver():
    print(f"{Fore.LIGHTGREEN_EX}\nEnter your Spotify token:{Fore.RESET}")  # prints in green
    spotify_api_token = input()
    print(f"{Fore.LIGHTBLUE_EX}")

    # Get a list of all the playlists from YouTube
    youtube_client = YouTubeClient('private/client_secret.json')
    print(f"{Fore.RESET}\n")
    spotify_client = SpotifyClient(spotify_api_token)

    playlists = youtube_client.youtube_get_all_playlists()

    # Choose which playlist to extract songs from
    print(f"{Fore.LIGHTBLUE_EX}These are all of your YouTube Playlists{Fore.RESET}\n")  # prints in blue
    for index, playlist in enumerate(playlists):
        print(f"{index} - {Fore.LIGHTRED_EX}{playlist.title}{Fore.RESET}")  # title prints in red

    print(f"{Fore.LIGHTBLUE_EX}\nEnter the playlist number:{Fore.RESET}")  # in blue
    number = int(input())
    playlist = playlists[number]
    print(f"\nYou selected - {Fore.LIGHTRED_EX}{playlist.title}{Fore.LIGHTMAGENTA_EX}\n")  # title prints in red

    songs = youtube_client.youtube_songs_in_playlist(playlist.id)
    print(f"{Fore.RESET}\n")
    # Search for the song on spotify. If we found the song, add it to our Spotify liked songs
    for song in songs:
        spotify_song_id = spotify_client.spotify_song_search(song.artist, song.song_name)
        if spotify_song_id:
            song_added = spotify_client.spotify_add_song(spotify_song_id)
            if song_added:
                print(f"{Fore.RESET}Successfully added {Fore.LIGHTGREEN_EX}{song.song_name}{Fore.RESET}"
                      f" by {Fore.LIGHTBLUE_EX}{song.artist}{Fore.RESET} to your Spotify liked songs playlist!")


if __name__ == '__main__':
    driver()

