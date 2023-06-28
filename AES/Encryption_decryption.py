# A python code for the encryption by using AES.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text, AES.block_size)
    return plaintext

# Generate a random 16-byte key for AES-128
key = get_random_bytes(16)

# Example usage
plaintext = b"Hello, AES"

# Encrypt the plaintext
encrypted_text = encrypt(key, plaintext)
print("Encrypted Text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt(key, encrypted_text)
print("Decrypted Text:", decrypted_text)