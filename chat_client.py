from sbnLIB import ChatClient
import threading

def receive_messages(client):
    while True:
        message = client.receive()
        if message:
            print(f"{client.host}:{client.port} >>> {message}")

if __name__ == "__main__":
    client = ChatClient('127.0.0.1', 12345)
    client.connect()

    # Start a thread to listen for messages from the server
    listen_thread = threading.Thread(target=receive_messages, args=(client,))
    listen_thread.start()

    # Send messages to the server
    while True:
        message = input("Enter message: ")
        client.send_message(message)
