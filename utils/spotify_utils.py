import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from data.config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

def get_spotify_titles(playlist_url):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    ))

    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    playlist = sp.playlist(playlist_id)

    name = playlist["name"]
    owner = playlist["owner"]["display_name"]
    description = playlist.get("description", "")
    cover_url = playlist["images"][0]["url"] if playlist["images"] else None
    track_items = playlist["tracks"]["items"]
    titles = [f"{t['track']['name']} {t['track']['artists'][0]['name']}" for t in track_items]

    return {
        "name": name,
        "owner": owner,
        "description": description,
        "cover_url": cover_url,
        "titles": titles,
        "count": len(titles)
    }
