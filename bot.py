import speech_recognition as sr
import pyttsx3 as p
from web_automation import *;
from wiki import *;
r = sr.Recognizer()
engine=p.init();
engine.say("What you would like me to do ?")
engine.runAndWait()
with sr.Microphone() as source:
    print("SAY>>>>")
    text =r.listen(source);
    try:
        recognise_text = r.recognize_google(text)
    except sr.UnknownValueError:
        print(" ")
    except sr.RequestError as e:
        print("")
    str=recognise_text.split(' ');
    print(str)
    if(str[0]=='info'):
        bot=info();
        bot.get_info(str[1])