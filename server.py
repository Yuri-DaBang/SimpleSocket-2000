from sbnLIB import SocketServer

class MyServer(SocketServer):
    def handle_client(self, client_socket, client_address):
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"Received data from {client_address}: {data}")
                # Process the received data as needed
                client_socket.sendall("Message received by server".encode())
        except Exception as e:
            print(f"Error occurred with client {client_address}: {e}")
        finally:
            client_socket.close()

server = MyServer('127.0.0.1', 12345)
server.start()
