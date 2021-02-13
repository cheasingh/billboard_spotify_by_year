import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from pprintpp import pprint as pp


class SpotifyManager:
    def __init__(self):

        # authenticate via OAuth
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope="playlist-modify-private ,user-follow-modify",
            redirect_uri="http://example.com",
            client_id=os.environ["SPOT_ID"],
            client_secret=os.environ["SPOT_SEC"],
            show_dialog=True,
            cache_path="token.txt"
        ))

        self.user_id = self.sp.current_user()['id']
        self.playlist_id = ""

    def search_song(self, track):
        # artist = self.sp.artist(
        #     "https://open.spotify.com/artist/0fauHpmSHwodVYIjTqOGHz?si=sFpqeWGuSe6JHDMsSVGniw")

        # pp(artist)
        song = self.sp.search(q=track, type="track", limit=1, market=None)

        # pp(song)
        try:
            song['tracks']['items'][0]['id']

        except IndexError:
            print(f"{track} not found")
            return False

        else:
            return song['tracks']['items'][0]['id']

    def create_playlist(self, name):
        playlist = self.sp.user_playlist_create(
            user=self.user_id, name=name, public=False, description="from api")

        self.playlist_id = playlist["id"]

    def delete_playlist(self):
        self.sp.user_playlist_unfollow(self.user_id, "66ecHzfujMfPxZQqyIfBHL")
        pp("done!")

    def add_track(self, tracks):
        self.sp.user_playlist_add_tracks(
            self.user_id, playlist_id=self.playlist_id, tracks=tracks)
        pp("done!")
