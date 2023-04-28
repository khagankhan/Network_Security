# Diffie-Hellman Key Exchange with MITM Attack Demonstration

This repository contains a demonstration of the Diffie-Hellman (DH) key exchange protocol and a Man-in-the-Middle (MITM) attack on the protocol. The DH key exchange is a method for securely establishing a shared secret between two parties (Alice and Bob) over a public channel. However, DH does not provide authentication, making it vulnerable to MITM attacks.

## Repository Structure

- `client.py`: Represents Alice, the client, and performs the DH key exchange with the server (Bob).
- `server.py`: Represents Bob, the server, and performs the DH key exchange with the client (Alice).
- `trudy.py`: Represents Trudy, the attacker, who intercepts and modifies the communication between Alice and Bob.
- `helper.py`: Contains helper functions for printing the output.

## How to Run

1. Clone this repository to your local machine.
2. Open three separate terminal windows.
3. In the first terminal window, navigate to the repository folder and run the server (Bob) using the command: `python3 client.py`
4. In the second terminal window, navigate to the repository folder and run Trudy using the command: `python3 trudy.py`
5. In the third terminal window, navigate to the repository folder and run the client (Alice) using the command: `python3 client.py`


The output will display the original shared keys for Alice and Bob. Then change port number from client side to connect to Trudy (from 12346 to 12345 in client.py). This way Alice (client.py) will connect to Trudy. The output in this case will demonstrate Trudy's shared keys with both parties, demonstrating that Trudy has changed them. Alice and Bob's messages will be intercepted and modified by Trudy.

## Note

This demonstration is for educational purposes only. To make the DH key exchange more secure and protect against MITM attacks, consider using public key infrastructure (PKI) or other authentication mechanisms in combination with the DH key exchange.


