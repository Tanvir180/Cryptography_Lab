
# def checkMultiplicativeinverse(a, n):
#     r1 = n
#     r2 = a
#     s1 = 1
#     s2 = 0
#     t1 = 0
#     t2 = 1
#
#     while r2 > 0:
#         q = int(r1 / r2)
#         r = r1 - q * r2
#         r1 = r2
#         r2 = r
#
#         s = s1 - q * s2
#         s1 = s2
#         s2 = s
#
#         t = t1 - q * t2
#         t1 = t2
#         t2 = t
#
#     t = t1
#
#     if r1 == 1:
#         return t
#     else:
#         return " "


def Decryption(ciphertext, key):
    result = ""
    inverse = pow(7,-1,26)
    # inverse = checkMultiplicativeinverse(key, 26)
    #
    # if inverse != " ":
    #     if inverse != " " and int(inverse) < 0:
    #         inverse = inverse + 26
    #     elif inverse != " " and int(inverse) >= 0:
    #         inverse = inverse
    #     else:
    #         print("Multiplicative inverse is not possible for this pair")

    for i in range(len(ciphertext)):
            char = ciphertext[i]

            if char == ' ':
                result += char
            elif char.isupper():
                value = ord(char) - 65
                result += chr((((value * inverse) % 26) + 65) + 32)
            else:
                value = ord(char) - 97
                result += chr(((value * inverse) % 26) + 97)
    return result


input = open("output.txt", "r+")
output = open("input.txt", "w")

result = Decryption(input.read(), 7)
input.truncate(0)

output.write(result)

input.close()
output.close()