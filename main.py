print('''
        |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
        |«««««««««««««««« ‡ FRIDAY ‡ »»»»»»»»»»»»»»» |
        |«««««««««« ‡ Artificial-Intelligence ‡ »»»»»»»»»»|
        |««««««««««««««««««-by Lokesh Tak »»»»»»»»»»» |
        |_______________________________________| ''')

# Note : Replacing my name with yours Won't make you Genius !
#======================================================================================#
import pyttsx3                                                  #pip install pyttsx3
import speech_recognition as sr                       #pip install speech_recognition
import webbrowser                                            #pip install webbrowser
import wikipedia                                                #pip install wikipedia
import mysql.connector                                     #pip install mysql
import random 
import datetime
import os
import pyjokes

#======================================================================================#
webbrowser.register('browser', None,
webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
#======================================================================================#
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#======================================================================================#
db=mysql.connector.connect(host='localhost',user='root',passwd='hello')
curser=db.cursor()
#======================================================================================#
def speak(audio):
    tk.Label(text=audio).place(x=300,y=300)
    tk.Label(text='').place(x=300,y=300)
    window.update()
    engine.say(audio)
    engine.runAndWait()
#======================================================================================#
def wishme(a):
    date=datetime.datetime.now().date()
    day=datetime.datetime.now().strftime('%A')
    time=datetime.datetime.now().strftime("%H:%M:%S")
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak('Good Morning Sir !')
    elif hour>=12 and hour<18 :
        speak('Good Afternoon Sir !')
    else:
        speak('Good Evening Sir !')
    speak(f'''
                                                                                              {day}
                                                                                              {date}
                                                                                              {time}''')
    lst=['I am Friday. please tell me how may I assist you !',
         'Friday by Lokesh Tak, at your service sir.',
         'How can I help you Sir ?',
         'Welcome to friday virtual assistant program, what can I do for you sir...!']
    R=random.randrange(0,len(lst))
    speak(lst[R]) 
#======================================================================================#
def takecommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening sir.........!")
        r.pause_threshold=1
        r.energy_threshold = 186
        r.dynamic_energy_threshold = False
        audio=r.listen(source)
        
        
        try:
            print('Recognizing...wait for a while.')
            query=r.recognize_google(audio,language='en-in')
            print(f"Your Command:{query}")

        except Exception as e:
            print("I didn't get it. Please say that again Sir...!")
            return "None"
    return query
#======================================================================================#

#======================================================================================#
wishme()
n=0
while True :
    query=takecommand().lower()
#======================================================================================#
    if query=='friday':
        speak('Yes sir, here I am')
    if query=='hello' or query=='hello friday' or query=='hi' or query=='hi friday':
        speak('hello sir !')
    if query==("what's up buddy"):
        speak("I'm fine sir.")
    if query=='thanks' or query=='thank you' or query=='thanks friday' or query=='thank yoy friday':
        lst=['You are welcome SIR.','no problem',"That's my Job sir."]
        R=random.randrange(0,len(lst))
        speak(lst[R])
#======================================================================================#
    query=query.replace('friday ',"")
    query=query.replace(' friday',"") 
#======================================================================================#
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        if query != '' :
            try :
                results = wikipedia.summary(query, sentences=2)                                 #WIKIPEDIA
                speak("According to Wikipedia")
                speak(results)
            except Exception as e :
                speak("couldn't find any data ")
        else:
            print('Please Enter something to search...!')
        continue
#======================================================================================#
    if ('open' and '.com')  in query:
        query=query.replace('open ','')
        query=query.replace(' ','')
        speak('opening '+query+' for you...')                                                              #BROWSER
        webbrowser.get('browser').open_new_tab(f"https://www.{query}")
        continue
#======================================================================================#
    if 'make' and 'me' and 'laugh' in query or query=='jokes':
        speak('This is a nice one, hope you like it.')
        speak(pyjokes.get_joke(language='en',category='all'))
#======================================================================================#
    if query=='play some music' or query=='play music':
        music_dir ='F:\\New folder\\Audio'
        speak('Hope this one is your favourite.')
        songs = os.listdir(music_dir)                                                                           #MUSIC
        R=random.randint(0,len(songs)-1)
        os.startfile(os.path.join(music_dir, songs[R]))
        continue
#======================================================================================#
    if query=='stop the music' or query=='stop music':
        speak('Got it sir...!')
        os.system("taskkill /f /im  vlc.exe")
        continue
#======================================================================================#
    if query=='time' or query=="what's the time"   :
        strTime = datetime.datetime.now().strftime("%H:%M:%S")                         #TIME     
        speak(f"Sir, the time is {strTime}")
        continue
#======================================================================================#
    if query=='open mysql' or query=='open sql' :
        speak('opening mySQL')
        codePath1 = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL"
        codePath2="\MySQL Server 8.0\MySQL 8.0 Command Line Client"
        codePath=codePath1+codePath2
        os.startfile(codePath)
        continue
#======================================================================================#
    if query=='open brave' or query=='open grave':
        speak('opening  Brave')
        codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(codePath)
        continue

#======================================================================================#
    if query=='open python' or query=='open idle':
        speak('opening IDLE')
        codePath1="C:\\ProgramData\Microsoft\Windows\Start Menu"
        codePath2="\Programs\Python 3.10\IDLE (Python 3.10 64-bit).lnk"
        codePath=codePath1+codePath2
        os.startfile(codePath)
        continue
#======================================================================================#
    if query=='shut up' or query=='bye' or query=='exit':
        lst=['Ok sir... Have a nice day','Friday powering off in 3.  2.  1. ','Always ready to help sir']
        R=random.randrange(0,len(lst))
        speak(lst[R])
        os.system("taskkill /f /im  pythonw.exe")
        break
#======================================================================================#
    if "search" and "database" in query:
        speak("which database sir")
        database=takecommand().lower()
        try:
            curser.execute(f"use {database}")
        except Exception as e:
            speak(f"couldn't find any database with name {database}")
            continue
        speak("say table name")
        table=takecommand().lower()
        try:
            curser.execute(f"select * from {table}")
            re=curser.fetchall()
            speak('Here is your data sir...!')
            for c in re:
                print(c)
            print()
        except:
            speak(f"there is no table with name {table}")
        continue
#======================================================================================#
    if "*" in query:
        speak('mind your language sir...!')
        continue
#======================================================================================#
    if query=='search' or query=='search online' :
        speak('what is to be searched sir ?')
        query=takecommand().lower()
        webbrowser.get('browser').open_new_tab(f"https://www.google.com/search?q={query}")
        speak('hope this is what you are looking for...!')
        continue
#======================================================================================#
    if query=='help':
        print('''
    1. wikipedia "Topic"
    2. open "website" .com
    3. Play or stop music
    4. Time
    5. open or close sql,brave,python
    6. Exit
    7. search database
    8. search online
    9. make a note or read it 
                    ''')
        continue
#======================================================================================#
    if "close" in query:
        query=query.replace('close',"")
        speak(f'closing {query}')
        os.system(f"taskkill /f /im  {query}.exe")
#======================================================================================#
    if query=='make a note':
        speak('what should be the name of note ?')
        name=takecommand().lower()
        note=open(f"{name}.txt",'w')
        speak('what is to be noted sir ?')
        info=takecommand()
        note.write(info)
        speak('Noted the above info successfully.')
        note.close()
        continue
#======================================================================================#
    if query=='read a note':
        speak('which note sir ?')
        name=takecommand().lower()
        try:
            note=open(f'{name}.txt','r')
            speak('Just a minute sir...!')
            info=note.read()
            speak(info)
            note.close()
        except Exception as e:
            speak ('There is no file with such name sir , please try again...!')
        continue
#======================================================================================#            
    else:
        continue
