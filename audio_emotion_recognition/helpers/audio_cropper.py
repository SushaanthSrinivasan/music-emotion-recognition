import os
from pydub import AudioSegment 

err = []

filenames = os.listdir('./tracks_v2')
for filename in filenames:
    try:
        if os.path.isfile(f"./cropped_tracks_v2/{filename.split('_')[-1]}"):
            print(f"{filename.split('_')[-1]} exists") 
            continue
        else:
            song = AudioSegment.from_file(f'./tracks_v2/{filename}', format="mp3") 
            half = len(song) / 2
            thirty_seconds = 30 * 1000
            middle_60_seconds = song[half-thirty_seconds : half+thirty_seconds] 
            
            middle_60_seconds.export(f"./cropped_tracks_v2/{filename.split('_')[-1]}", format="mp3") 
            print(f"{filename.split('_')[-1]} created") 
    except:
        err.append(filename.split('_')[-1])

with open('crop_err.txt', 'w') as file:
    file.write(str(err))
