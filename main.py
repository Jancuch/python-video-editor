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
            if loopinfo != 0 :
            	clip = VideoFileClip(video).subclip(0, loopinfo[2])
            	clip1 = VideoFileClip(video).subclip(loopinfo[0] , loopinfo[1])
            
            	loopcount1 = 0 
            	
            	clip1 = loop(clip1 ,loopcount)
            	countlooptime = loopinfo[1] - loopinfo[0] 
            	countlooptime = countlooptime * loopcount + loopinfo[2]
            
            	clip = concatenate_videoclips([clip , clip1])
            else:
            	clip = VideoFileClip(video)
            (w, h) = clip.size

            clip = crop(clip, width=800, height=800, x_center=w/2, y_center=h/2 )
            if loopinfo != 0 :
            	clip = clip.set_audio(audio1)
            	clip = clip.subclip(0, countlooptime)
            
            if audio:
                audio = AudioFileClip(audio)
                clip = clip.set_audio(audio)
                if loopinfo != 0:
                	clip = clip.subclip(0 , countlooptime)
                else:
                	clip = clip.subclip(0 , clip.duration)
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
        if loopinfo and loopcount:
        	ren = videocut(video , loopinfo , loopcount, audio)
        else:
        	ren = videocut(video ,loopinfo , loopcount, audio)
        if image:
        	ren = addImage(ren , image)
        render(ren)

    def imagegen(self, txt , fsize):
        new_txt = []
        letter_count = 0 
        for letter in txt:
            new_txt.append(letter)
            letter_count = letter_count + 1 
            if letter_count == 20:
                new_txt.append('\n')
                letter_count = 0

                
                
        print(new_txt)
        stringconv = ''.join(map(str , new_txt))
        print(stringconv)
        image = Image.open('./data/images/plz.png')
        font = ImageFont.truetype(r'./data/arial.ttf' , fsize)
        
        draw = pil.Draw(image)
        draw.text((20 , 0 ) , stringconv , fill=(20,20,20) , align='center' , font=font )
        print(image.size[0])
        #draw.text(txt)
        
        
        path = './data/images/plz1.png'
        image = image.save('./data/images/plz1.png')
        return path
        

meme = memegen()
img =meme.imagegen( 'Jebac Natana' , 70)
meme.videogen("./data/videos/pyro.mp4" ,audio="./data/audio/5g.mp3",  image=None , loopinfo=0 , loopcount=1)













