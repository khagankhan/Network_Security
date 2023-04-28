# client.py
import socket
from helper import print_output

g = 1907
p = 784313
S_A = 160031

def main():
    host = '127.0.0.1'
    port = 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    A = pow(g, S_A) % p
    client_socket.sendall(str(A).encode())

    B = int(client_socket.recv(1024).decode())
    shared_key = pow(B, S_A) % p
    print_output('Alice\'s Original Shared Key', str(shared_key) + ".")
    message = "Hello, Bob!"
    print_output("Alice's Original Message", message)
    client_socket.sendall(message.encode())

    modified_message = client_socket.recv(1024).decode()
    print_output("Message from Bob", modified_message)

    client_socket.close()

if __name__ == '__main__':
    main()

