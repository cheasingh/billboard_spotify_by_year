import requests
from bs4 import BeautifulSoup
import re
from spotify import SpotifyManager
from tqdm import tqdm


date_search = input("when do you want to get back? 'YYYY-MM-DD': ")

sp = SpotifyManager()

# tracks_id = []


def play_by_year(date):
    response = requests.get(
        f"https://www.billboard.com/charts/hot-100/{date}").text
    soup = BeautifulSoup(response, "html.parser")

    song_list = [song.getText() for song in soup.select(
        "span.chart-element__information__song.text--truncate.color--primary")]
    # print(song_list)

    year = date.split("-")[0]
    sp.create_playlist(f"Billboard top 100 - {year}")
    # print(sp.playlist_id)

    # print()
    add_track_to_playlist(find_track(song_list))


def find_track(track):

    tracks_id = []
    for i in tqdm(track):
        search = sp.search_song(i)
        if search == False:
            print(search)
        else:
            tracks_id.append(search)

    return tracks_id


def add_track_to_playlist(tracks):
    sp.add_track(tracks)


if re.match(r"[0-9][0-9][0-9][0-9]+-+[0-1][0-9]+-+[0-3][0-9]+", date_search):
    play_by_year(date_search)
else:
    print("please make sure your input is follow the requested format\nex: 1999-02-14")
