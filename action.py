import datetime
import speak
import webbrowser
import weather
import os

def Action(send) :   
  
    if send is not None:
         data_btn = send.lower()
    else:
         data_btn = ""


    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hey" in data_btn  or "hay" in data_btn or "hii" in data_btn: 
        speak.speak("Hey sir, How can I  help you !")  
        return "Hey sir, How can I help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great sir") 
            return "I am doing great sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("it's my pleasure sir")
           return "its my pleasure sir"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shut down" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or 'music' in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("enjoy your music")                   
        return "Enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google opened")  
        return "google opened"

    elif 'you tube' in data_btn or "open you tube" in  data_btn or "youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube opened") 
        return "YouTube opened"    
    
    elif 'weather' in data_btn or 'whether' in data_btn:
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'offline song' in data_btn:
        url = "C:\\Users\\DELL\\Downloads\\birds39-forest-20772.mp3"
        os.startfile(url)
        speak.speak("file opened")
        return "file opened" 

    else :
        speak.speak( "I'm unable to understand!")
        return "I'm unable to understand!"       
