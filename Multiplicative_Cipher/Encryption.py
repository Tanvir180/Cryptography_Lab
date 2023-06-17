# A python code for the encryption and decryption of text by the Ciser cipher technique.

def encryption(plaintext, key):
    result = ""

    # This for loop is for the traverse the text.
    for i in range(len(plaintext)):
        char = plaintext[i]

        # This condition is for the "space" that means if plain text contain space it remains on the cipher text.
        if char == ' ':
            result += char
        # This condition is for the "Upper Case" Letter Their ascii value start from 65.
        elif char.isupper():
            result += chr((((ord(char) -65) * key) % 26) + 65)
        # This condition is for the "Lower case latter" their ascii value start from 97.
        else:
            result += chr(((((ord(char) - 97) * key) % 26) + 97) - 32)   # Ekane 32 minuse kora hoice capital letter dekhate cipher text xapital letter hoy

    return result


input = open("input.txt", "r+")
output = open("output.txt", "w")
plaintxt = input.read();
key = 7;
result = encryption(plaintxt, key)
output.write(result)
# Next two line is for the truncating the file.
input.truncate(0)

input.close()
output.close()