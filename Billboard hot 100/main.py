import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import base64
from bs4 import BeautifulSoup
date =input(("Which year do you want to travel to? Type date in this format YYYY-MM-DD: "))
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
music_bill = response.text
soup = BeautifulSoup(music_bill,"html.parser")

music = soup.select(selector="li h3")
music_list = [music[i].getText() for i in range(0,100)]

new_lsit = [ i.strip() for i in music_list]
print(new_lsit)
billboard_text = response.text

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)



user_id = sp.current_user()["id"]
api_links = []
year = date.split("-")[0]
print(year)
for i in new_lsit:
    results = sp.search(q=f"track:{i},year:{year}",type='track')
    print(results)
    try:
        links = results["tracks"]["href"]
        api_links.append(links)
    except IndexError:
        print(f"The song {i} is not avaible on spotify")
playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=True)
print(playlist["id"])
print(api_links)
sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist["id"],tracks=api_links, position=None)
