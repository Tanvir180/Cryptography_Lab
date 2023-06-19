# A python code for the encryption by using AES.
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the plaintext and key
# A byte string, also known as a bytes literal, is a sequence of bytes.
# It represents raw binary data and is generally used to handle non-textual or binary data, such as images, audio files, or network protocols.
plaintext = b'This is a secret message'

# In Python, the get_random_bytes() function is typically provided by a cryptographic library, such as Crypto.Random from the pycryptodome library or secrets module from the standard library.
# The get_random_bytes() function takes a parameter that specifies the desired length of the random byte string to generate.In this case, the parameter is 16, which corresponds to 16 bytes or 128 bits.
key = get_random_bytes(16)

# Create an AES cipher object with a 128-bit key
# This three parameter and last parameter which may vary from mode to mode.
# If CRT Mode it must pass the initial vector counter(IV).
cipher = AES.new(key, AES.MODE_EAX)  # (Authenticated Encryption with Associated Data, Xor).

# Encrypt the plaintext
# The tag variable represents the authentication tag that is generated during the encryption process using an authenticated encryption mode like AES.MODE_EAX.
# The authentication tag provides a unique identifier for the encrypted data, ensuring that it has not been tampered with or modified.
# During decryption, the authentication tag is also recalculated based on the decrypted ciphertext, the secret key, and the associated data.
# The calculated authentication tag is compared with the received authentication tag.
# If the calculated tag matches the received tag, it indicates that the ciphertext has not been tampered with and is authentic. The receiver can trust the integrity of the decrypted data.
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Print the encrypted ciphertext and tag
print("Ciphertext:", ciphertext)
print("Ciphertext :",base64.b64encode(ciphertext))
print("Tag:", tag)


# Decryption

# Create a new AES cipher object with the same key
# The nonce (number used once) is a crucial component in symmetric key encryption algorithms, particularly in modes like AES.MODE_EAX.
# It serves as an additional input to the encryption algorithm and helps ensure the uniqueness and security of the ciphertext produced.
decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)

# Decrypt the ciphertext
decrypted_plaintext = decrypt_cipher.decrypt_and_verify(ciphertext, tag)

# Print the decrypted plaintext
print("Decrypted plaintext:", decrypted_plaintext.decode())