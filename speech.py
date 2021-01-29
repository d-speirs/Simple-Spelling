from gtts import gTTS 
import datetime
import pygame
import os
import time

def PlayWord(word):
  pygame.mixer.init()
  currentTime = datetime.datetime.now()
  day = currentTime.strftime("%d")
  hour =  currentTime.strftime("%H")
  minute = currentTime.strftime("%M")
  second = currentTime.strftime("%S")
  outputFileName = 'input' + str(day) + str(hour) +str(minute) +str(second) + '.mp3'

  soundObj = gTTS(text=word, lang='en', slow=False) 
  soundObj.save(outputFileName) 

  pygame.mixer.music.load(outputFileName)
  pygame.mixer.music.play()
  time.sleep(1.5)
  pygame.mixer.music.stop()
  pygame.quit()

  # delete the audio file 
  try:
    os.remove(outputFileName)
  except:
    pass



