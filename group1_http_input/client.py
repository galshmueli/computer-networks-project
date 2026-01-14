import socket

SERVER_IP = "172.20.10.10"  
SERVER_PORT = 10004
BUFFER_SIZE = 1024


def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")

        welcome_msg = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        print(f"Server says: {welcome_msg}")

        while True:
            user_input = input("Type message to send (or 'exit' to quit): ")

            if user_input.lower() == "exit":
                print("Closing connection...")
                break

            client_socket.sendall(user_input.encode("utf-8"))

            server_response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            print(f"Response from server: {server_response}")

    except ConnectionRefusedError:
        print("Could not connect to server. Is it running?")

    finally:
        client_socket.close()


if __name__ == "__main__":
    run_client()
