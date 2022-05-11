from datetime import datetime
import Pyro5.server

@Pyro5.server.expose
class Chat(object):
    def handle_client(value, msg):
        print(f'[{datetime.now():%H:%M:%S}] -> {msg}')

def start():
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.core.locate_ns()
    uri = daemon.register(Chat)
    ns.register('teste', str(uri))
    print(f'Listening...')
    daemon.requestLoop()

if __name__ == '__main__':
    try:
        start()
    except(KeyboardInterrupt, EOFError):
        print('GoodBye')
exit