import os
#welcome credits
print("Welcome to Video bitrate changer (vbc) "
      "FFMPEG is used to done this")
#taking inputs
bitrate = input("Enter a bitrate number like 16k, 17000k normally all videos are on 17000k: ")
path = input("Path to video file: ")

os.system(f"ffmpeg.exe -i {path} -b:v {bitrate} output.mp4")