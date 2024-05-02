import os
from dotenv import load_dotenv
import pandas as pd
from dotify import Dotify, models
from tqdm import tqdm

load_dotenv()

spotify_id = os.getenv('SPOTIFY_ID')
spotify_secret = os.getenv('SPOTIFY_SECRET')

df = pd.read_csv("./data/muse_v3.csv")
err = []

url = "https://open.spotify.com/track/2hsLpiKNkWpd4e9QuVdhar"

with Dotify():
    track = models.Track.from_url(url)
    track.download(f"./test/test.mp3")