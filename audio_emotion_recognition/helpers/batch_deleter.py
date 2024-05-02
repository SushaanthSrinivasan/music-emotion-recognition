import os

files = os.listdir('./tracks_v2')
for file in files:
    if '2RTq8bwkb5qXGFp1B077Xu' in file:
        print(f"Removing track: {file}")
        os.remove(f"./tracks_v2/{file}")