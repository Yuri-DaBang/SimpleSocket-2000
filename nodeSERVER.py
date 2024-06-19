import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def handle_client(self, client_socket, client_address):
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"Received data from {client_address}: {data}")
                # Process the received data as needed
        except Exception as e:
            print(f"Error occurred with client {client_address}: {e}")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)

    def start(self, backlog=5):
        self.socket.bind((self.host, self.port))
        self.socket.listen(backlog)
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                client_socket, client_address = self.socket.accept()
                print(f"Connection established with {client_address}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()
                self.clients.append(client_socket)
        except KeyboardInterrupt:
            print("Server program terminated by user.")
        finally:
            self.close()

    def close(self):
        print("Closing server...")
        for client_socket in self.clients:
            client_socket.close()
        self.socket.close()

if __name__ == "__main__":
    server_host = '127.0.0.1'  # Set your server host here
    server_port = 12345         # Set your server port here
    
    server = Server(server_host, server_port)
    server.start()
