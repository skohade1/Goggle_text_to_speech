# from gtts import gTTS
# import os
# mytext='welcome to the saurabh'
# language='en'
# myobj=gTTS(text=mytext, lang=language)
# myobj.save('welcome.mp3')
# os.system('start welcome.mp3')






from gtts import gTTS
import os 
input('enter your email to get registered: ')
tts = gTTS('welcome', lang='en')
tts.save('welcome.mp3')
os.system("welcome.mp3")
print('Hey, your emailid is registered successfully... :) ')