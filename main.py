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
            audio1 = audio1.volumex(0)
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
            video = video.write_videofile('./output/output2.mp4', codec='libx264', audio=True, audio_codec='aac')

        ren = videocut(video , loopinfo , loopcount, audio)
        ren = addImage(ren , "./data/images/ask.png")
        render(ren)

    def imagegen(self, txt , fsize):
        new_txt = []
        letter_count = 0 
        for letter in txt:
            new_txt.append(letter)
            letter_count = letter_count + 1 
            if letter_count == 19:
                new_txt.append('\n')
                letter_count = 0
                
                
        print(new_txt)
        stringconv = ''.join(map(str , new_txt))
        print(stringconv)
        image = Image.open('./data/images/ask.png')
        font = ImageFont.truetype(r'./data/arial.ttf' , fsize)
        
        draw = pil.Draw(image)
        draw.text((30 , 0 ) , stringconv , fill=(255,255,255) , align='center' , font=font )
        print(image.size[0])
        #draw.text(txt)
        
        image.show()
        
        image = image.save('./data/images/ask1.png')
        return image
        

meme = memegen()
img =meme.imagegen( '0123456789012345678901234567890sssssssssssssssssssssssssssssssssssssssssssss' , 70)
meme.videogen("./data/videos/pyro.mp4" ,audio=None,  image="./data/images/plz1" , loopinfo=[10 , 20 ,23] , loopcount=10)













