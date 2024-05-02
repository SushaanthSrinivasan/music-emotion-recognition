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

try:
    with Dotify():
        for idx, row in df.iloc[6247:].iterrows():
            try:
                track = models.Track.from_url(f"https://open.spotify.com/track/{row['spotify_id']}")
                track.download(f"./tracks/{idx}_{row['spotify_id']}.mp3")
                print(f'Done upto index {idx}')
                if idx == 10000:
                    break
            except Exception as e:
                print(e)
                err.append(idx)
                continue
except KeyboardInterrupt:
    with open("err_indices.txt", "w") as output:
        output.write(str(err))

with open("err_indices.txt", "w") as output:
    output.write(str(err))