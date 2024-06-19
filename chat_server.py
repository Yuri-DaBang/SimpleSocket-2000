from sbnLIB import ChatServer

class MyChatServer(ChatServer):
    def __init__(self, host, port):
        super().__init__(host, port)

server = MyChatServer('127.0.0.1', 12345)
server.start()