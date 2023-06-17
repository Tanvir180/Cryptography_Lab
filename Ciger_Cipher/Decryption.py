# A python code for the decryption of the text by the Ciser cipher technique.
def decryption(ciphertext, key):
    result = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        # This condition is for the "space" that means if plain text contain space it remains on the cipher text.
        if char == ' ':
            result += char
        # This condition is for the "Upper Case" Letter Their ascii value start from 65.
        elif char.isupper():
            result += chr(((((ord(char) - key) - 65) % 26) + 65)+32)   # 32 add kora hoyece lower case dekhate
        # This condition is for the "Lower case latter" their ascii value start from 97.
        else:
            result += chr((((ord(char) - key) - 97) % 26) + 97)
    return result


input = open("output.txt", "r+");
output = open("input.txt", "w");
ciphertext = input.read();
key = 17;
result = decryption(ciphertext, key)
output.write(result)
# Next two line is for the truncating the file.
input.truncate(0)

input.close()
output.close()