from moviepy.editor import *
from moviepy.video.fx.all import crop
clip = VideoFileClip("./data/videos/pyro.mp4").subclip(0 , 23)
audio = AudioFileClip("./data/audio/reposted.mp3")
clip1 = VideoFileClip("./data/videos/pyro.mp4").subclip(10 ,20)

final = concatenate_videoclips([clip , clip1 , clip1, clip1, clip1, clip1])
final = crop(final , x1=175   ,y1=150)
final1 = final.set_audio(audio)

final1.write_videofile("./output/e-pyro.mp4")
final2 = VideoFileClip("./output/e-pyro.mp4").subclip(1 , 40)
final2.write_videofile("./output/e-pyro1.mp4")