from moviepy.editor import *
from moviepy.video.fx.all import crop
clip = VideoFileClip("./data/videos/pyro.mp4").subclip(0 , 23)
audio = AudioFileClip("./data/audio/reposted.mp3")
clip1 = VideoFileClip("./data/videos/pyro.mp4").subclip(10 ,20)

logo = ImageClip("./data/images/ask.png")

logo = logo.resize((800,100)) # if you need to resize...
#logo.margin(right=8, top=8, opacity=0) # (optional) logo-border padding
logo = logo.set_position(("center","top"))


final = concatenate_videoclips([clip , clip1 , clip1, clip1, clip1, clip1])

(w, h) = clip.size
print(w , h)
final = crop(final, width=800, height=800, x_center=800, y_center=800)
final = final.set_audio(audio)
final = CompositeVideoClip([final, logo.set_duration(final.duration)])
final = final.subclip(0 , 40)
final.write_videofile("./output/e-pyro.mp4")
