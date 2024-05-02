import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
import numpy as np

df = pd.read_csv('./data/muse_v3.csv', low_memory=False)
df.drop(df.index[10001:], axis=0, inplace=True)
df.dropna(subset=['spotify_id'])

filenames = []
for idx, row in df.iterrows():
    print(idx)
    filenames.append(f"{idx}_{row['spotify_id']}.mp3")

df["filename"] = filenames

err = []

try:
    for idx, row in tqdm(df.iloc[4482:].iterrows(), total=len(df)):
        try:
            filename = row["filename"]
            y, sr = librosa.load(f'./tracks/{filename}', sr=None)
            mel = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2560, hop_length=512, n_mels=256, fmin=20, fmax=16000)
            mel_db = librosa.power_to_db(mel, ref=np.max)

            fig, ax = plt.subplots()
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
            ax.set_frame_on(False)
            librosa.display.specshow(mel_db, sr=sr)
            plt.savefig(f"./images/{row['filename']}.png", dpi=400, bbox_inches='tight', pad_inches=0)
            plt.close('all')
        except Exception as e:
            err.append(idx)
except KeyboardInterrupt:
    with open('err.txt', 'w') as file:
        file.write(str(err))

with open('err.txt', 'w') as file:
    file.write(str(err))