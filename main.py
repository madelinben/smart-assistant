import speech_recognition

def respond(responseString):
    print(responseString)

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
        respond()

if __name__ == '__main__':
    while True:
        listen()