def respond(responseString):
    print(responseString)

def process():
    query = None
    return query

def listen():
    command = process()
    
    if not command:
        respond('Could you say that again please.')
    else:
        respond()

if __name__ == '__main__':
    while True:
        listen()