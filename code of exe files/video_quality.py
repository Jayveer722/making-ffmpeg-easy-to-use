import os

# Welcome credits
print("Welcome to Video Quality Enchancer "
      "There are 3 types of Quality are supported "
      "4K, 1080p(UHD), 720p "
      "FFMPEG is used to done this")
# taking tpe of quality and destination of the file which needed to be convert into higher quality or lower quality
user_input = input("Which type of quality do you need: ")
path_to_file = input("Path to video file: ")
# These are the types of quality
k = "4k"
uhd = "1080p"
p = "720p"
pp = "480p"
ppp = "360p"
qp = "240p"
qqp = "144p"

# Using if elif to run specfic command for specfic type of quality

if (user_input == k):
    os.system(F"ffmpeg -i {path_to_file} -vf scale=2160:1440 video_4K.mp4")
elif (user_input == uhd):
    os.system(f"ffmpeg -i {path_to_file} -vf scale=1920:1080 video_uhd.mp4")
elif (user_input == p):
    os.system(f"ffmpeg -i {path_to_file} -vf scale=1280:720 video_720p.mp4")
elif (user_input == pp):
    os.system(f"ffmpeg -i {path_to_file} -vf scale=720:480 video_480p.mp4")
elif (user_input == ppp):
    os.system(f"ffmpeg -i {path_to_file} -vf scale=480:360 video_360p.mp4")
elif (user_input == p):
    os.system(f"ffmpeg -i {path_to_file} -vf scale=426:240 video_240p.mp4")
elif (user_input == qqp):
    os.system(f"ffmpeg -i {path_to_file} -vf scale=256:144 video_144p.mp4")
else:
    print("Not supported")
