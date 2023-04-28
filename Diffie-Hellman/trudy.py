# trudy.py
import socket
import threading
from helper import print_output

g = 1907
p = 784313
secret_t = 4567

def trudy_to_bob(trudy_socket, bob_socket):
    A = int(trudy_socket.recv(1024).decode())
    T_to_B = pow(g, secret_t) % p
    bob_socket.sendall(str(T_to_B).encode())
    B = int(bob_socket.recv(1024).decode())
    T_to_A = pow(g, secret_t) % p
    trudy_socket.sendall(str(T_to_A).encode())

    shared_key_t_b = pow(B, secret_t) % p
    shared_key_t_a = pow(A, secret_t) % p
    print_output("Trudy's shared keys", f"With Alice: {shared_key_t_a}, With Bob: {shared_key_t_b}")

    message_from_alice = trudy_socket.recv(1024).decode()
    print_output("Message from Alice", message_from_alice)

    modified_message = "Trudy's message to Bob"
    print_output("Trudy's Modified Message", modified_message)
    bob_socket.sendall(modified_message.encode())

    message_from_bob = bob_socket.recv(1024).decode()
    print_output("Message from Bob", message_from_bob)

    modified_message = "Trudy's message to Alice"
    print_output("Trudy's Modified Message", modified_message)
    trudy_socket.sendall(modified_message.encode())

def main():
    host = '127.0.0.1'
    alice_port = 12345
    bob_port = 12346

    trudy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    trudy_socket.bind((host, alice_port))
    trudy_socket.listen(1)
    print_output('Trudy Info', f'Listening for Alice on port: {alice_port}')

    alice_conn, addr = trudy_socket.accept()
    print_output('Connection Info', f'Connected to Alice: {addr}')

    bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bob_socket.connect((host, bob_port))

    trudy_to_bob(alice_conn, bob_socket)

    alice_conn.close()
    bob_socket.close()

if __name__ == '__main__':
    main()

