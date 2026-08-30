import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

def play_song():
  '''
  This function will be used to make a call to the spotify api to play marvin's
  room from Drake
  '''
  # define all the client requirements
  CLIENT_ID = os.getenv("CLIENT_ID")
  CLIENT_SECRET = os.getenv("CLIENT_SECRET")
  REDIRECT_URI = "http://localhost:8000"

  scope = "user-modify-playback-state"

  # authenticate the user
  sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
      client_id=CLIENT_ID,
      client_secret=CLIENT_SECRET,
      redirect_uri=REDIRECT_URI,
      scope=scope,
    )
  )

  # marvins room song id on spotify
  marvins_room_uri = "spotify:track:040g6Y44YgclCgA78v7X7N"

  # attempt to play the song on the authenticated users account
  try:
    # play the song because of the memes
    sp.start_playback(uris=[marvins_room_uri])

    # put that shit on repeat
    sp.repeat("track")
    print("Now playing: Marvin's Room 🎧")

  except spotipy.exceptions.SpotifyException as e:
    # if an error occurs, then just enjoy being single.
    # it's actually not that bad
    print(f"An error occurred: {e}")
    print(
      "Make sure you have a Spotify app open and active on one of your devices!"
    )
