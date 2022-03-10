import pyttsx3
import urllib.request,bs4 as bs,sys,threading
from tkinter import scrolledtext, ttk
import tkinter as tk
from PIL import ImageTk
import PIL.Image
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from tkinter import *
import subprocess as sub
import speech_recognition as sp

paths={'notepad':r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad'}

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def open_camera():
    sub.run('start microsoft.windows.camera:', shell=True)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:

        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am faaz assistant. Please tell me how may I help you") 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id', to, content)
    server.close()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def mainframe():
    """Logic for execution task based on query"""
    greet()
    query_for_future=None

    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")

        elif 'open code' in query:
            codePath = "put path of visual studio"
            os.startfile(codePath)

        elif 'email to mumtaz' or 'mail to mumtaz' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your friend's mail id"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")  

        elif 'open camera' in query:
            open_camera()           
        
        elif 'open notepad' in query:
            os.startfile(paths['notepad'])

            

def gen(n):
    for i in range(n):
        yield i

class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        mainframe()

def Launching_thread():
    Thread_ID=gen(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()

if __name__=="__main__":
     #tkinter code
    root=tk.Tk()
    style = ttk.Style(root)
    current_theme = style.theme_use("alt")
    
    root.geometry("{}x{}+{}+{}".format(500,260,int(root.winfo_screenwidth()/2 - 745/2),int(root.winfo_screenheight()/2 - 360/2)))
    root.resizable(0,0)
    root.title("Virtual_Assistant")
    img = PhotoImage(file=r'C:\Users\user\Downloads\\Microphone-icon.png')
    root.tk.call('wm', 'iconphoto', root._w, img) 
    frameCnt = 20
    frames = [PhotoImage(file=r'C:\Users\user\Downloads\BasicFaithfulBirdofparadise__1__AdobeCreativeCloudExpress.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(90, update, ind)
    label = Label(root)
    root.after(0, update, 0)
    label.pack()

    Listen_Button=tk.Button(root,borderwidth=0,activebackground='#000000',command=Launching_thread)
    Listen_Button.place(x=242,y=125)
    
    Listen_Button.place(x=242,y=125)
    myMenu=tk.Menu(root)
   
    Speak_label=tk.Label(root,text="SPEAK:",fg="#000000",font='"Times New Roman" 20 ',borderwidth=0)
    Speak_label.place(x=50,y=110)
    
    
    root.config(menu=myMenu)
    
    
    root.mainloop()