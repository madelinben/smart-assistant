import speech_recognition
import pyttsx3
import datetime
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def respond(responseString):
    engine.say(responseString)
    engine.runAndWait()

def process():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)

    try:
        print('Processing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'Query: {query}.\n')
    except Exception as exception:
        print(exception)
        print('Could you say that again please.')
        return None
    
    return query

def listen():
    command = process().lower()
    
    if not command:
        respond('Could you say that again please.')
    else:
        if ('hi' in command) or ('hello' in command):
            respond('Hello world.')
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A %d %B %Y')
            respond('Todays date is ' + date + '.')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            respond('The current time is ' + time + '.')
        elif 'joke' in command:
            respond(pyjokes.get_joke())

if __name__ == '__main__':
    while True:
        listen()