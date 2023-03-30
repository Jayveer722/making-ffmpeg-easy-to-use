import os
#welcome credits
print("Welcome to Video Scale Changer (vsc) "
      "Th scale you want we will change the video scale to that "
      "FFMPEG is used to done this")
#inputs
user_input = input("Which scale do you want for example 2160:1440 for (4K) enter the value like this: ")
path_to_file = input("Path to video file: ")
#conversion
os.system(f"ffmpeg -i {path_to_file} -vf scale={user_input} video.mp4")