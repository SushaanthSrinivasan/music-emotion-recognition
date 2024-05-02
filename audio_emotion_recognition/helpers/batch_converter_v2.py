import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from tqdm.notebook import tqdm
import pandas as pd
import numpy as np
import os

df = pd.read_csv('./df_test.csv', low_memory=False)
err = []

try:
    for idx, row in df.iterrows():
        try:
            filename = f"{row['spotify_id']}.mp3"
            print(f"Converting song with id {row['spotify_id']}")
            y, sr = librosa.load(f'./cropped_tracks_v2/{filename}', sr=None)
            mel = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=sr*3, hop_length=512, n_mels=256, fmin=20, fmax=16000)
            mel_db = librosa.power_to_db(mel, ref=np.max)
            fig, ax = plt.subplots()
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
            ax.set_frame_on(False)
            librosa.display.specshow(mel_db, sr=sr)
            plt.savefig(f"./df_test/{filename[:-4]}.png", dpi=400, bbox_inches='tight', pad_inches=0)
            plt.close('all')
        except Exception as e:
            err.append(filename)
except KeyboardInterrupt:
    with open('converter_err_v2.txt', 'w') as file:
        file.write(str(err))

with open('converter_err_v2.txt', 'w') as file:
    file.write(str(err))