# Secret Key Encryption and Decryption

This is a Python program that implements secret key encryption and decryption based on the following requirements:

- The program must take an array of 8 characters as input and output an array of 8 encrypted characters.
- The code necessary to create 8 unique random substitution tables, one for each character of the array, is included.
- The program must use a 64-bit key (can be represented as another array of 8 characters) derived from an 8-character password.
- Encryption algorithm:
  - Take the input array and XOR it with the key.
  - Using the XORed output, perform a character-by-character substitution using the different substitution tables.
  - Perform the permutation step once after the substitution step.
  - For the permutation step, circular shift the bit pattern by one to the left with the leftmost bit becoming the rightmost bit.
  - Repeat the above steps 16 times, corresponding to 16 rounds, with the output of a round serving as the input for the next round.
- Decryption algorithm:
  - Reverse the encryption algorithm.
  - The permutation should circular shift the bit pattern by 1 bit to the right.
  - The substitution tables are also used for reversing the substitution.
- For more information check `Task.pdf`

To run the program, execute the `secret_key.py` file. The program will prompt you to input an 8-character string to encrypt and decrypt. The program will output the original input, the encrypted output, and the decrypted output for the input string. 


This simple method is vulnerable in the face of some attacks which I will show practically in the future. You can think how Trudy can break this algorithm.

You can try to implement this in Java!

Enjoy your secret key encryption and decryption!
