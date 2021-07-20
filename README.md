# Wikipedia-Bot
This is Simple Wikipedia bot
It include 2 Python Script
1) bot.py = This is the Script use to call the class info present in wiki.py
            it recognise the user Speech and Convert it into text and if the User Says "Info (Anything)"
            it will Call class info present in wiki.py
            it uses library like SpeechRecognition(to Convert Speech to text) and pyttsx3(to convert text to Speech)
            Also, it Uses Google Api to recognise Speech
2) wiki.py = This Script Contain the Class info which is used to find the information about the parameter which is passed
             into get_info() 
             it contains library like Selenium for Automatically invoking Chrome browser and getting information from wikipedia
             about the parameter Passed into the function
 
           
