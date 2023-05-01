import random
import datetime

# Left rotate a byte
def leftRotate(x):
    return (((x << 1) & 0xFF) | (x >> (7)))

# Right rotate a byte
def rightRotate(x):
    return ((x >> 1)) | ((x << (7) & 0xFF))

# Generate substitution table
def substitutiontable(seed_value):
    random.seed(seed_value)
    availMapping = list(range(256))
    encryptTable = {}
    decryptTable = {}
    mapLeft = 256
    for i in range(256):
        rand = random.randint(0, mapLeft - 1)
        encryptTable[i] = availMapping[rand]
        decryptTable[availMapping.pop(rand)] = i
        mapLeft -= 1
    return encryptTable, decryptTable

# Make n substitution tables
def makeSubTables(n):
    subTables = []
    for i in range(n):
        subTables.append(substitutiontable(datetime.datetime.now().timestamp() + i))
    return subTables

subtables = makeSubTables(8)

# Encrypt the input array using the given key
def encrypt(inputarray, key):
    inputIntArray = [ord(char) for char in inputarray]
    keyIntArray = [ord(char) for char in key]
    xoredArray = []
    for i in range(8):
        xoredArray.append(inputIntArray[i] ^ keyIntArray[i])
    subArray = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(8):
        subArray[i] = subtables[i][0][xoredArray[i]]
    outputArray = subArray
    for i in range(8):
        for j in range(16):
            outputArray[i] = leftRotate(outputArray[i])
    outputCharArray = [chr(num) for num in outputArray]
    return outputCharArray

# Decrypt the encrypted array using the given key
def decrypt(outputArray, key):
    keyIntArray = [ord(char) for char in key]
    outputIntArray = [ord(char) for char in outputArray]
    permArray = outputIntArray
    for i in range(8):
        for j in range(16):
            permArray[i] = rightRotate(permArray[i])
    subArray = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(8):
        subArray[i] = subtables[i][1][permArray[i]]
    orignalIntArray = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        orignalIntArray[i] = subArray[i] ^ keyIntArray[i]
    orignalArray = [chr(num) for num in orignalIntArray]
    return orignalArray

def main():
    input_array = input("Enter an 8-character input string: ")
    if len(input_array) != 8:
        print("Error: Input string must be 8 characters long.")
        return

    key = input("Enter an 8-character key: ")
    if len(key) != 8:
        print("Error: Key must be 8 characters long.")
        return

    # Encryption and decryption process
    output_array = encrypt(input_array, key)
    decrypted_array = decrypt(output_array, key)

    # Print input, encrypted, and decrypted output
    print(f"Input Array: {input_array}")
    print(f"Encrypted Output: {''.join(output_array)}")
    print(f"Decrypted Output: {''.join(decrypted_array)}")

    # Testing with a slightly modified input array
    input_array2 = input_array[:-1] + ('z' if input_array[-1] != 'z' else 'y')
    output_array2 = encrypt(input_array2, key)
    decrypted_array2 = decrypt(output_array2, key)

    # Print input, encrypted, and decrypted output for the modified input array
    print(f"Input Array: {input_array2}")
    print(f"Encrypted Output: {''.join(output_array2)}")
    print(f"Decrypted Output: {''.join(decrypted_array2)}")

if __name__ == "__main__":
    main()

