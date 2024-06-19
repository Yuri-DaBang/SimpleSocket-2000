from sqlite3 import ProgrammingError
import socket
import threading
import os



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

if __name__ == "__main__":
    client = SocketClient('127.0.0.1', 12345)
    client.connect()
    client.send_whoami_with_ip_periodically()