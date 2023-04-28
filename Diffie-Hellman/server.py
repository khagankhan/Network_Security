# server.py
import socket
from helper import print_output

g = 1907
p = 784313
S_B = 12077

def main():
    host = '127.0.0.1'
    port = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print_output('Server Info', 'Listening on port: {0}'.format(port))

    conn, addr = server_socket.accept()
    print_output('Connection Info', 'Connected by: {0}'.format(addr))

    A = int(conn.recv(1024).decode())
    B = pow(g, S_B) % p
    conn.sendall(str(B).encode())

    shared_key = pow(A, S_B) % p
    print_output('Bob\'s Original Shared Key', str(shared_key) + ".")
    message = "Hello, Alice!"
    print_output("Bob's Original Message", message)
    conn.sendall(message.encode())

    modified_message = conn.recv(1024).decode()
    print_output("Message from Alice", modified_message)

    conn.close()

if __name__ == '__main__':
    main()

