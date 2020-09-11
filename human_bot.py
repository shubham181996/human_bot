import pyttsx3 
import os

#pyttsx3.speak("Hello Shubham, I am AI bot, what kind of help you")

while True:

 print("Hello there, what kind I can assist you :"  , end='')
 p = input()
 #print(p)

 if (("run" in p) or ("execute" in p) and ("notepad" in p) or ("editor" in p)):
  os.system("notepad")
 
 elif (("run" in p) or ("execute" in p) and ("video player" in p) or ("watch" in p)):
  os.system("wmplayer")
 
 elif (("run" in p) or ("execute" in p) and ("internet" in p) or ("browser" in p)):
  os.system("chrome")
 
 elif ("exit" in p) or ("quit" in p):
  break
  
 else:
  print("Don't Support")
 