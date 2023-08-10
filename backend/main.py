import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime,random
import wikipedia
import webbrowser
import PyPDF2
import sys,os

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source,duration=1) # Adjust for ambient noise
            voice = listener.listen(source,0,10)
            print('Recognizing')
            global command
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said : {command} \n")
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print(command)

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.UnknownValueError:
        pass
    return command

def play_song(song):
    talk('Playing ' + song)
    pywhatkit.playonyt(song)

def get_time():
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Sir, the time is {time}")
def get_date():
        date = datetime.date.today().strftime("%B %d, %Y")
        talk(f"Sir,today's date is {date}")
def get_day():
        day = datetime.datetime.now().strftime('%A')
        talk(f"Sir, today is {day}")

def get_wikipedia_info(topic):
        info = wikipedia.summary(topic, 3)
        print(info)
        talk(info)

def location():
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        talk("This is your current location")

def place():
        url = 'https://google.nl/maps/place/' + command[command.find('of')+3:]+'/&amp'
        webbrowser.get().open(url)

def google():
        webbrowser.open("google.com")
        talk("here you go to google")

def youtube():
        webbrowser.open("youtube.com")
        talk("here you go to youtube")

def pdfReader():
        pdf = open('C:\MainProjects\Voice assistant\Hacking_ the art of exploitation.pdf','rb')
        textReader= PyPDF2.PdfFileReader(pdf)
        singlePage=textReader.getPage(19)
        text=singlePage.extractText()
        talk(text)

def music():
        music_dir = "C:\\Users\\pvish\\Music"
        songs = os.listdir(music_dir)
        index = random.randint(0, 30)
        os.startfile(os.path.join(music_dir, songs[index]))
        talk("playing music from your device")

def male():
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        talk("Voice changed to male")

def female():
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    talk("Voice changed to female")





def stop():
    talk("Bye,Sir will meet you later")
    sys.exit(0)

def run_assistant():



    command = take_command()
    command= command.lower()

    if 'play' in command:
        song = command.replace('play', '')
        play_song(song)

    elif "what is the time" in command:
        get_time()

    elif "what is the date" in command:
        get_date()

    elif "what is the day today" in command:
        get_day()

    elif 'who is' in command:
        topic = command.replace('who is', '')
        get_wikipedia_info(topic)

    elif 'what is' in command:
        topic = command.replace('what is', '')
        get_wikipedia_info(topic)

    elif 'my location' in command:
        location()

    elif 'find location of' in command:
        place()

    elif 'open google' in command:
        google()

    elif 'open youtube' in command:
        youtube()

    elif 'read pdf' in command:
        pdfReader()

    elif 'listen music' in command:
        music()

    elif 'change your voice to male' in command:
        male()
		
    elif 'change your voice to female' in command:
        female()

    elif 'stop' in command:
        stop()

    else:
        talk('Sorry, I did not understand that. Please say the command again.')

    while True:
    	run_assistant()
