from moviepy.editor import *
from moviepy.video.fx.all import crop , loop
from PIL import Image, ImageFont, ImageDraw as pil

class memegen():


    def videogen(self , video , audio , image , loopinfo , loopcount):
        clip = VideoFileClip(video).subclip(0 , loopinfo[2])
        clip1 = VideoFileClip(video).subclip(loopinfo[0] , loopinfo[1])
        audio = AudioFileClip(audio)
        image = ImageClip(image)
        image = image.set_position(("center","top"))
        clip1 = loop(clip1 , loopcount)
        final = concatenate_videoclips([clip , clip1])
        (w, h) = clip.size
        final = crop(final, width=800, height=800, x_center=w/2, y_center=h/2)
        final = final.set_audio(audio)
        final = CompositeVideoClip([final, image.set_duration(final.duration)])
        countlooptime = loopinfo[1] - loopinfo[0] 
        countlooptime = countlooptime * loopcount + loopinfo[2]
        final = final.subclip(0 , countlooptime)
        final.write_videofile("./output/output.mp4")
    
    def imagegen(self, path , txt , size , orientation):
        image = Image.open(path)
        draw = pil.ImageDraw(image)
        size1 = size
        font = ImageFont.truetype(r'./data/arial.ttf' , size=size1)
        txt1 = txt
        draw.text((5,5),font=font , align=orientation , text=txt1)
        image.show()
        image = image.save('./data/images/ask1.png')
        return path

meme = memegen()
meme.imagegen('./data/images/ask.png' , '       robert kiedy \n     kupuje gry w "nizu" ', 40 , "center")
meme.videogen("./data/videos/pyro.mp4" , "./data/audio/reposted.mp3", "./data/images/ask1.png" , [10 , 20 ,23] , 6)













