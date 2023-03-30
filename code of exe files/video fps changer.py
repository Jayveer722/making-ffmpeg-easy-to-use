import os
#welcome credits
print("Welcome to Video Fps changer (vfc) "
      "FFMPEG is used to done this")

#taking inputs from user
fps = input("Enter a fps number: ")
path = input("Path to video file: ")

os.system(f"ffmpeg -i {path} -r {fps} output.mp4")