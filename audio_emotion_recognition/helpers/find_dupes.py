import pandas as pd
import os

df = pd.read_csv('./df_train.csv', low_memory=False)
l = []

for idx, row in df.iterrows():
    filename = row["spotify_id"] + ".png"
    l.append(filename)
    if os.path.isfile(f'./df_train/{filename}'):
        continue
    else:
        print(filename)

seen = set()
dupes = [x for x in l if x in seen or seen.add(x)]       
print(dupes)