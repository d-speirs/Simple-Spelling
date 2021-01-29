import speech
import time
import datetime
import random
from random import seed
from random import randint

def startGame(randomOrder):
  # seeding based on the second of the current time
  time_current = datetime.datetime.now().strftime("%S")
  seed(int(time_current))
  wordlist = 'wordlist.txt'
  incorrectWordsFile = 'incorrectwords.txt'

  index = 0 
  finalIndex = 0
  testWord = ''
  lines = []

  print('Type "stop" to exit')

  with open(wordlist, 'r') as sourceWordsList:
    lines = sourceWordsList.readlines() 
    finalIndex = len(lines)-1

  while (index <= finalIndex) or (randomOrder == True):
    if randomOrder == True:
      testWord = random.randint(0,len(lines)-1)
    else:
      testWord = (lines[index])

    speech.PlayWord(testWord)
    typedText = input("Type word: ")

    if typedText.strip().lower() == 'stop':
      break

    if (typedText.strip().lower() == testWord.strip().lower()):
      speech.PlayWord("Correct")
      time.sleep(0.5)
    else:
      speech.PlayWord("Incorrect")
      writeToIncorrectWordList = True

      with open(incorrectWordsFile, 'r') as f:
        for line in f:
          if line.strip().lower() == testWord.strip().lower():
            writeToIncorrectWordList = False
            break

      if writeToIncorrectWordList == True:
        with open(incorrectWordsFile, "a") as text_file:
          text_file.write(testWord.strip().lower() + '\n')

      print("Incorrect: " + testWord.strip())
      time.sleep(0.5)

    index += 1 

  print('Program ended')