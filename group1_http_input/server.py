import socket
import threading

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 10004


def client_handler(client_socket, client_address):
    print(f"New connection from {client_address}")

    try:
        welcome_message = "Welcome to the server"
        client_socket.sendall(welcome_message.encode("utf-8"))

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode("utf-8")
            print(f"Message from {client_address}: {message}")

            reply = f"Server received: {message.upper()}"
            client_socket.sendall(reply.encode("utf-8"))

    except ConnectionResetError:
        print(f"Client {client_address} disconnected unexpectedly")

    finally:
        print(f"Closing connection with {client_address}")
        client_socket.close()


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()

    print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()

        thread = threading.Thread(
            target=client_handler,
            args=(client_socket, client_address)
        )
        thread.start()

        print(f"Active clients: {threading.active_count() - 1}")


if __name__ == "__main__":
    run_server()
