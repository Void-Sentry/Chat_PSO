import Pyro5.api

server = Pyro5.api.Proxy(f'PYRONAME:teste')

def send():
    while True:
        message = input('-> ')
        if message == 'exit':
            break
        server.handle_client(message)

if __name__ == '__main__':
    try:
        send()
    except(KeyboardInterrupt, EOFError):
        print('GoodBye')
exit