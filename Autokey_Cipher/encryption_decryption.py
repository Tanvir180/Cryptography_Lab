#This program will encrypt the message using autokey cipher
#Fuction for generating the keystream
def generateKeyStream(plainText, key):
    result = key
    for i in range(len(plainText) - 1):
        result += plainText[i]
    return result

#Encryption function
def encrypt(message, key):
    result = ""
    for i in range(len(message)):
        messageChar = message[i]
        keyStreamChar = key[i]
        #Main formula: cipherText = (plainText + keyStream) mod 26
        if messageChar.isupper():
            result += chr(((ord(messageChar) - 65) + (ord(keyStreamChar) - 65)) % 26 + 65)
        elif messageChar.islower():
            result += chr(((ord(messageChar) - 97) + (ord(keyStreamChar) - 97)) % 26 + 97)
        else: ##If we have space as character, then just concatenate it
            result += messageChar

    return result

#Decryption function
def decrypt(message, key):
    result = ""
    for i in range(len(message)):
        messageChar = message[i]
        keyStreamChar = key[i]
        # Main formula: plainText = (cipherText - keyStream) mod 26
        if messageChar.isupper():
            result += chr(((ord(messageChar) - 65) - (ord(keyStreamChar) - 65)) % 26 + 65)
        elif messageChar.islower():
            result += chr(((ord(messageChar) - 97) - (ord(keyStreamChar) - 97)) % 26 + 97)
        else: ##If we have space as character, then just concatenate it
            result += messageChar

    return result

def main():
    plainText = input("Enter the plainText: ")
    autoKey = input("Enter the autoKey: ")
    keyStream = generateKeyStream(plainText, autoKey)
    #Printing the keyStream
    print(f"Key Stream : {keyStream}")
    ciphertext = encrypt(plainText, keyStream)
    print(f"Encrypted ciphertext: {ciphertext}")
    decryptedPlainText = decrypt(ciphertext, keyStream)
    print(f"Decrypted PlainText: {decryptedPlainText}")

if __name__ == "__main__":
    main()
