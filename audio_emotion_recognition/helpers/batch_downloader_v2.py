import os
from dotenv import load_dotenv
import pandas as pd
from dotify import Dotify, models

load_dotenv()

spotify_id = os.getenv('SPOTIFY_ID')
spotify_secret = os.getenv('SPOTIFY_SECRET')

df = pd.read_csv("./data.csv")
err = []

try:
    with Dotify():
        for idx, row in df.iterrows():
            try:
                track = models.Track.from_url(row['spotify'])
                filename = row['spotify'].split(',')[-1].split('/')[-1]
                track.download(f"./tracks_v2/{idx}_{filename}.mp3")
                print(f'Done upto index {idx}')
            except Exception as e:
                print(e)
                err.append(idx)
                continue
except KeyboardInterrupt:
    with open("err_indices_v2.txt", "w") as output:
        output.write(str(err))

with open("err_indices_v2.txt", "w") as output:
    output.write(str(err))
