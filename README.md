# YouTube-to-Spotify
Automates the transfer of music from YouTube playlists to your Spotify 'Liked Songs' playlist. Uses YouTube and Spotify's web API's to retrieve the users information.

1) import requests
   import google_auth_oauthlib.flow
   import googleapiclient.discovery
   import youtube_dl
   
2) Authenticate with the Youtube Data API.
  This link provides you with the code snippet needed to access a YouTube users information through the API: https://developers.google.com/youtube/v3/code_samples/code_snippets
  Use this link obtain authorization credentials for the project and download the JSON file: https://developers.google.com/youtube/registering_an_application
  Store the JSON file in seperate folder and pass that information in 
     --> flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(--> ENTER JSON CRED FILE HERE <--, scopes) from the code snippet
     
3) Create functions to get the users playlists, get the songs in those playlists, and get the artist/song name from each song. (see my code provided)

4) Authenticate with Spotify's Data API
  Log in to your spotify account using this link: https://developer.spotify.com/
  Search "save tracks for current user" and request an OAUTH TOKEN. *Make sure to check the box "user-library-modify"*
  Save that OAUTH TOKEN for later
 
5) Create functions to search for songs on Spotify and add songs to Spotify playlists. (see my code provided)

6) Put it all together!
  Use the Spotify API key and YouTube JSON file credentials to create Spotify and YouTube client Objects.
  Ask the user which YouTube playlist they would like to transfer to spotify, and use the functions to make it happen!
    (obtain all the YouTube playlists, get the songs/artists info from the chosen playlist, search for each song on Spotify, add it on Spotify)
    
