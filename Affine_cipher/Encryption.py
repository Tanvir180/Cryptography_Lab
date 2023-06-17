def encryption(plaintext, key1):
    result = ""

    # This for loop is for the traverse the text.
    for i in range(len(plaintext)):
        char = plaintext[i]

        # This condition is for the "space" that means if plain text contain space it remains on the cipher text.
        if (char == ' '):
            result += char
        # This condition is for the "Upper Case" Letter Their ascii value start from 65.
        elif (char.isupper()):
            result += chr(((((ord(char)-65)*key1) + key2) % 26) + 65)
        # This condition is for the "Lower case latter" their ascii value start from 97.
        else:
            result += chr(((((ord(char)-97)*key1) + key2) % 26) + 97)

    return result


input = open("input.txt", "r+")
output = open("output.txt", "w")
plaintxt = input.read()
key1 = 7
key2 = 2
result = encryption(plaintxt, key1)
output.write(result.upper())
# Next two line is for the truncating the file.
input.truncate(0)

input.close()
output.close()