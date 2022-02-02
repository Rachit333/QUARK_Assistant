# Created by Rachit Jasoria
# Follow on Github: https://bit.ly/rachit_at_github
import speech_recognition as sr
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options;
import os
import socket
import time
import pyttsx3


engine = pyttsx3.init(driverName='sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',500.0)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

chrome_path = r"C:\Windows\chromedriver.exe"
options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')

def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

if is_connected() is False:
    engine.say(" please check The Internet Connection and Try Again")
    engine.runAndWait()
    print("Check The Internet Connection and Try Again!!")

elif is_connected() is True:
    driver = webdriver.Chrome(chrome_path, options=options)
    engine.say("hey i am pav, your pesonal assistant! ")
    engine.runAndWait()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.1)
        audio= r.listen(source)
        wake = r.recognize_google(audio)
        if 'hello' in wake:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                myname = "Strager" #change to your name
                r.adjust_for_ambient_noise(source,duration=0.1)
                engine.say("how can i help you" +myname+ "?")
                engine.runAndWait()
                audio= r.listen(source)
                voice_data = r.recognize_google(audio)

if 'search' in voice_data:
    engine.say("what do you want to search "+myname)
    engine.runAndWait()
    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source,duration=0.1)
     audio= r.listen(source)
     search = r.recognize_google(audio)
     print("")
     url = 'https://www.google.com/search?q=' + search
     webbrowser.get().open(url)
     print("This is what you searched for: " + search)

elif 'find place' in voice_data:
    engine.say("which place do you want to search?"+myname)
    engine.runAndWait()
    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source,duration=0.1)
     audio= r.listen(source)
     searchplace = r.recognize_google(audio)
     print("")
     url = 'https://www.google.com/maps/place/' + searchplace
     webbrowser.get().open(url)
     print("This is the place you searched for: " + searchplace)

elif 'weather' in voice_data:
    engine.say("showing weather reports of India")
    engine.runAndWait()
    url = 'https://www.accuweather.com/en/in/india-weather'
    webbrowser.get().open(url)

elif 'YouTube' in voice_data:
    engine.say("which video would you like to see?"+myname)
    engine.runAndWait()
    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source,duration=0.1)
     audio= r.listen(source)
     searchvideo = r.recognize_google(audio)
     url = 'https://www.youtube.com/results?search_query=' + searchvideo
     webbrowser.get().open(url)
     print("This is the video you searched for: " + searchvideo)

elif 'music' in voice_data:
    engine.say("which music would you like to hear?"+myname)
    engine.runAndWait()
    song_name = input("::")
    name = "https://gaana.com/search/"+song_name
    driver.get(name)

    driver.find_element_by_class_name("hover-events-parent").click()

elif 'change song' in voice_data:
    song_name = input("::")
    name = "https://gaana.com/search/"+song_name
    driver.get(name)

    driver.find_element_by_class_name("hover-events-parent").click()


elif 'computer' in voice_data:
    engine.say("please  paste  the  folder  path  here  to  see  it's  files"+myname)
    engine.runAndWait()
    find = input('HERE==>  ')
    l = os.listdir(find)
    for e in l:
        print(e)

elif 'calculate' in voice_data:
    engine.say("please enter first integer"+myname)
    engine.runAndWait()
    print("FIRST INTEGER: ")
    x = int(input())
    engine.say("please enter second integer"+myname)
    engine.runAndWait()
    print("SECOND INTEGER:")
    y = int(input())
    engine.say(f" what do you want to do with{x} and {y}")
    engine.runAndWait()
    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source,duration=0.1)
     audio= r.listen(source)
     calqltr = r.recognize_google(audio)
     if 'multiply' in calqltr:
         z=x*y
         print(f"{x} into {y} is equal to {z}")
         engine.say(f"{x} into {y} is equal to {z}")
         engine.runAndWait()

     if 'subtract' in calqltr:
         z=x-y
         print(f"{x} minus {y} is equal to {z}")
         engine.say(f"{x}minus{y} is equal to{z}")
         engine.runAndWait()


     if 'divide' in calqltr:
         z=x/y
         print(f"{x} upon {y} is equal to {z}")
         engine.say(f"{x}upon{y} is equal to{z}")
         engine.runAndWait()

     if  'addition' in calqltr:
         z=x+y
         print(f"{x} plus {y} is equal to {z}")
         engine.say(f"{x}plus{y} is equal to{z}")
         engine.runAndWait()

elif 'note' in voice_data:
    with sr.Microphone() as source:
     print("SPEAK NOW TO MAKE A NOTE" +myname)
     r.adjust_for_ambient_noise(source,duration=0.1)
     audio= r.listen(source)
     note = r.recognize_google(audio)
     print(note)
     fh = open('demo.txt','a')
     fh.write(f'{note}\n\n')
     fh.close


elif 'code' in voice_data:
      os.system('start microsoft.windows.camera:')

elif 'chrome' in voice_data:
    os.startfile("C://Program Files (x86)\Google\Chrome\Application\chrome.exe")

elif 'camera' in voice_data:
    os.system('start microsoft.windows.camera:')

elif 'skype' in voice_data:
    os.startfile("C:\Program Files (x86)\Skype\Phone\Skype.exe")

elif 'ppt' in voice_data:
    os.startfile("C://Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.exe")



elif 'to do' in voice_data:
    engine.say('these are your notes' +myname)
    engine.runAndWait()
    note = open("demo.txt","r+")
    notes = note.read()
    engine.say(notes)
    engine.runAndWait()

else:
    engine.say('no command found add in the code and try again')
    engine.runAndWait()
