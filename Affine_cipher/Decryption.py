def decryption(ciphertext, key1):
    result = ""
    mi=pow(key1,-1,26)
    # This for loop is for the traverse the text.
    for i in range(len(ciphertext)):
        char = ciphertext[i]

        # This condition is for the "space" that means if plain text contain space it remains on the cipher text.
        if (char == ' '):
            result += char
        # This condition is for the "Upper Case" Letter Their ascii value start from 65.
        elif (char.isupper()):
            result += chr(((((ord(char)-65)-key2)*mi) % 26) + 65)
        # This condition is for the "Lower case latter" their ascii value start from 97.
        else:
            result += chr(((((ord(char)-97)-key2)*mi) % 26) + 97)

    return result



input = open("output.txt", "r+")
output = open("input.txt", "w")
ciphertext = input.read()
key1 = 7
key2=2
result = decryption(ciphertext, key1)
output.write(result.lower())
# Next two line is for the truncating the file.
input.truncate(0)

input.close()
output.close()