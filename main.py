from moviepy.editor import *
from moviepy.video.fx.all import crop , loop
from PIL import Image, ImageFont, ImageDraw as pil
clip = VideoFileClip('./data/videos/pyro.mp4').subclip(0 , 10)

audio = AudioFileClip('./data/audio/co.mp3')


#final = clip
#(w, h) = clip.size
#final = crop(final, width=w/2, height=800, x_center=w/2, y_center=h/2)
#final = final.set_audio(audio)
#final = final.subclip(0 , clip.duration)
#
#final.write_videofile("./output/output.mp4",  codec='libx264', audio=True, audio_codec='aac')


class memegen():


    def videogen(self , video , audio , image , loopinfo , loopcount):
        
        def videocut(video , loopinfo , loopcount , audio):
            audio1 = AudioFileClip("./data/audio/lol.mp3")
            
            clip = VideoFileClip(video).subclip(0, loopinfo[2])
            clip1 = VideoFileClip(video).subclip(loopinfo[0] , loopinfo[1])
            
            loopcount1 = 0 
            print(loopcount)
            clip1 = loop(clip1 ,loopcount)
            countlooptime = loopinfo[1] - loopinfo[0] 
            countlooptime = countlooptime * loopcount + loopinfo[2]
            
            clip = concatenate_videoclips([clip , clip1])
            (w, h) = clip.size
            clip = crop(clip, width=800, height=800, x_center=w/2, y_center=h/2 )
            clip1 = clip1.set_audio(audio1)
            clip = clip.set_audio(audio1)
            clip = clip.subclip(0, countlooptime)
            
            if audio:
                audio = AudioFileClip(audio)
                clip = clip.set_audio(audio)
                clip = clip.subclip(0 , countlooptime)
            else:
                clip = clip
        
            return clip

        def addImage(video , image1):
            image = ImageClip(image1)
            image = image.set_position(("center","top"))
            video = CompositeVideoClip([video, image.set_duration(video.duration)])
            return video




        def render(video):
            video = video.write_videofile('./output/outpu1.mp4', codec='libx264', audio=True, audio_codec='aac')

        ren = videocut(video , loopinfo , loopcount, audio)
        ren = addImage(ren , "./data/images/ask.png")
        render(ren)
        #if image == None:
#
        #    clip = VideoFileClip(video).subclip(0 , loopinfo[2])
        #    clip1 = VideoFileClip(video).subclip(loopinfo[0] , loopinfo[1])
        #    audio = AudioFileClip(audio)
        #   
        #    clip1 = loop(clip1 , loopcount)
        #    final = concatenate_videoclips([clip , clip1])
        #    (w, h) = clip.size
        #    final = crop(final, width=w/2, height=800, x_center=w/2, y_center=h/2)
        #    final = final.set_audio(audio)
        #    countlooptime = loopinfo[1] - loopinfo[0] 
        #    countlooptime = countlooptime * loopcount + loopinfo[2]
        #    final = final.subclip(0 , countlooptime)
        #    final.write_videofile("./output/output.mp4")
#
        #if loopinfo:
        #    clip = VideoFileClip(video).subclip(0 , loopinfo[2])
        #    clip1 = VideoFileClip(video).subclip(loopinfo[0] , loopinfo[1])
        #    audio = AudioFileClip(audio)
        #    image = ImageClip(image)
        #    image = image.set_position(("center","top"))
        #    clip1 = loop(clip1 , loopcount)
        #    final = concatenate_videoclips([clip , clip1])
        #    (w, h) = clip.size
        #    
        #    final = crop(final, width=w/2, height=800, x_center=w/2, y_center=h/2)
        #    final = final.set_audio(audio)
        #    final = CompositeVideoClip([final, image.set_duration(final.duration)])
        #    countlooptime = loopinfo[1] - loopinfo[0] 
        #    countlooptime = countlooptime * loopcount + loopinfo[2]
        #    final = final.subclip(0 , countlooptime)
        #    final.write_videofile("./output/output.mp4")
        #
        #else:
        #    clip = VideoFileClip(video)
        #    image = ImageClip(image)
        #    image = image.set_position(("center","top"))
        #    (w, h) = clip.size
        #    final = VideoFileClip.subclip(0 , clip.duration)
        #    final = crop(final, width=800, height=800, x_center=w/2, y_center=h/2 -100)
        #    final = CompositeVideoClip([final, image.set_duration(final.duration)])
        #    final.write_videofile("./output/output.mp4")

    #def imagegen(self, path , txt , fsize , orientation):
    #    image = Image.open(path)
    #    draw = pil.ImageDraw(image)
    #    size1 = size
    #    font = ImageFont.truetype(r'./data/arial.ttf' , size=size1)
    #    txt1 = txt
    #    draw.text((5,5),font=font , align=orientation , text=txt1)
    #    image.show()
    #    
    #    image = image.save('./data/images/ask1.png')
    #    return path

meme = memegen()
#meme.imagegen('./data/images/ask.png' , '5', 65 ,  "center")
meme.videogen("./data/videos/pyro.mp4" , "./data/audio/5g.mp3",None , [10 , 20 ,23] , 5)













