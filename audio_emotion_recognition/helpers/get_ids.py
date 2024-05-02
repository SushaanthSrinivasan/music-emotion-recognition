import os

files = os.listdir('./tracks_v2')
for i in range(len(files)):
    files[i] = files[i].split('_')[-1][:-4]
    print(files[i])

with open("downloaded_spotify_ids.txt", "w") as output:
        output.write(str(files))
