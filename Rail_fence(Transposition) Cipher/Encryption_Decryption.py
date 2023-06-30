def rail_fence_encrypt(plaintext):
    p1 = ""
    p2 = ""
    ciphertext = ""
    for i in range(len(plaintext)):
        if (i % 2) == 0:
            p1 += plaintext[i]
        else:
            p2 += plaintext[i]
    ciphertext = p1 + p2
    return ciphertext, p1, p2


def rail_fence_decrypt(ciphertext, p1, p2):
    plaintext = ""
    for i in range(len(p1)):
        if p2[i] != '1':
            plaintext += p1[i] + p2[i]
        else:
            plaintext += p1[i]
    return plaintext


pt = input("Enter the plaintext : ")
plaintext = pt.replace(' ', '')

encrypted_message, p1, p2 = rail_fence_encrypt(plaintext)
print("Encrypted message:", encrypted_message.upper())

if len(p1) != len(p2):
    p2 += '1'

decrypted_message = rail_fence_decrypt(encrypted_message, p1, p2).lower()
print("Decrypted message:", decrypted_message)
