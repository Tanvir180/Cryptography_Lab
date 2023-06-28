# A python code for encryption by using the data encryption standard.

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# def pad(text):
#     # That means it will take 8,16,24 byte if the input is 6 byte it will take extra 2 byte
#     while len(text) % 8 != 0:
#         text += ' '
#     return text
def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text, DES.block_size)
    return plaintext

# Generate a random 8-byte key
key = get_random_bytes(8)

# byte string
plaintext = b"Hello, DES"

# Encrypt the plaintext
encrypted_text = encrypt(key, plaintext)
print("Encrypted Text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt(key, encrypted_text)
print("Decrypted Text:", decrypted_text)