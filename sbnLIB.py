import socket
import threading
import os

class SocketServer:
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
                client_socket.sendall("Message received by server".encode())
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

class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send(self, data):
        self.socket.sendall(data.encode())

    def receive(self, buffer_size=1024):
        return self.socket.recv(buffer_size).decode()

    def close(self):
        self.socket.close()

    def send_whoami_with_ip_periodically(self, interval=5):
        try:
            while True:
                whoami_output = subprocess.check_output(['whoami']).decode().strip()
                ip_address = self.get_ip()
                message = f"User: {whoami_output}, IP: {ip_address}"
                print(f"Sending: {message}")
                self.send(message)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Client program terminated by user.")
        except Exception as e:
            print(f"Error occurred: {e}")

    @staticmethod
    def get_ip():
        try:
            # Open a temporary socket to determine the local IP address
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            temp_socket.connect(("8.8.8.8", 80))  # Google DNS server
            ip_address = temp_socket.getsockname()[0]
            temp_socket.close()
            return ip_address
        except socket.error as e:
            print(f"Error while getting IP address: {e}")
            return None

class ChatServer(SocketServer):
    def __init__(self, host, port):
        super().__init__(host, port)

    def handle_client(self, client_socket, client_address):
        print(f"User connected from {client_address}")
        self.clients.append(client_socket)
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"Received message from {client_address}: {data}")
                self.broadcast(data)
        except Exception as e:
            print(f"Error occurred with client {client_address}: {e}")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)

    def broadcast(self, message):
        print(f"Broadcasting message to all clients: {message}")
        for client_socket in self.clients:
            try:
                client_socket.sendall(message.encode())
            except Exception as e:
                print(f"Error occurred while broadcasting message: {e}")

class ChatClient(SocketClient):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.received_message_ids = set()

    def listen_for_messages(self):
        try:
            while True:
                message = self.receive()
                if message:
                    message_parts = message.split(':')
                    message_id = message_parts[0]
                    message_text = ':'.join(message_parts[1:])
                    if message_id not in self.received_message_ids:
                        self.received_message_ids.add(message_id)
                        print(f"{self.host}:{self.port} >>> {message_text}")
        except KeyboardInterrupt:
            print("Client program terminated by user.")
        except Exception as e:
            print(f"Error occurred: {e}")

    def send_message(self, message):
        self.send(message)
     
class CommandServer:
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
                print(f"Received command from {client_address}: {data}")
                # Process the received command as needed
                response = self.execute_command(data)
                client_socket.sendall(response.encode())
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

    def execute_command(self, command):
        # Placeholder function for command execution logic
        return "Command execution result"


class NodeClient:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.socket.connect((self.server_host, self.server_port))
        print(f"Connected to server at {self.server_host}:{self.server_port}")

    def send_command(self, command):
        self.socket.sendall(command.encode())
        response = self.socket.recv(1024).decode()
        print("Response from server:", response)

    def close(self):
        self.socket.close()

class NodeServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                client_socket, client_address = self.socket.accept()
                print(f"Connection established with {client_address}")
                # Handle client commands and web usage reporting
        except KeyboardInterrupt:
            print("Server program terminated by user.")
        finally:
            self.close()

    def close(self):
        print("Closing server...")
        self.socket.close()