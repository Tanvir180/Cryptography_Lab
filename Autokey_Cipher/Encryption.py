# A python code for the encryption and decryption of text by the Ciser cipher technique.

def encryption(plaintext, key):
    result = ""
    j = 0

    # This for loop is for the traverse the text.
    for i in range(len(plaintext)):
        char = plaintext[i]

        if i==0:
            # For first key given
            if char.isupper():
                result += chr((((ord(char) + key) - 65) % 26) + 65)
            else:
                result += chr(((((ord(char) + key) - 97) % 26) + 97) - 32)

        else:
            # This condition is for the "space" that means if plain text contain space it remains on the cipher text.
            if char == ' ':
                result += char
                j = j+1

            # This condition is for the "Upper Case" Letter Their ascii value start from 65.
            elif char.isupper():
                char2 = plaintext[(i-j)-1]
                j = 0 # Current character er ager ta upper na lower check kora
                if char2.isupper():
                    akey = ord(char2) - 65
                else:
                    akey = ord(char2) - 97

                result += chr((((ord(char) + akey) - 65) % 26) + 65)
            # This condition is for the "Lower case latter" their ascii value start from 97.
            else:
                char2 = plaintext[(i-j) - 1]
                j = 0
                if char2.isupper():
                    akey = ord(char2) - 65
                else:
                    akey = ord(char2) - 97

                result += chr(((((ord(char) + akey) - 97) % 26) + 97) - 32)   # Ekane 32 minuse kora hoice capital letter dekhate cipher text xapital letter hoy

    return result


input = open("input.txt", "r+")
output = open("output.txt", "w")
plaintxt = input.read()
key = 12
result = encryption(plaintxt, key)
output.write(result)
# Next two line is for the truncating the file.
input.truncate(0)

input.close()
output.close()