# A python code for encryption by using the data encryption standard.

# Import the des function from the Crypto Module.

import base64
from Crypto.Cipher import DES

# This is the key for the encryption.
key = 'hello123'    #use as password

# This function is for the added the extra text to the plaintext if it is not fill
# The block of 64 bit's size.
def pad(text):
    # DES Algorithm works with 8 byte thats why we divided it by the 8.
    # If the given text is multiple of 8 then exit form the while loop.
    # That means it will take 8,16,24 byte if the input is 6 byte it will take extra 2 byte
    while len(text) % 8 != 0:
        text += ' '
    return text

# Create the object of the DES and pass the appropriate parameter.
# Second parameter is the encryption mode . Several encryption mode are available.
des = DES.new(key.encode('utf-8'),DES.MODE_ECB)  # 'utf-8' encode the string to bytes.As Des require the byte as parameter.

text = 'Tanvir Ahammed Hridoy'
padded_text = pad(text)

# This encrypt function is uesed to encrypt the message.
encrypted_text = des.encrypt(padded_text.encode('utf-8'))

print("The Encrypted text is :",encrypted_text)
print("The ecnrypted text in character formate :",base64.b64encode(encrypted_text))

# Create the object of the DES and pass the appropriate parameter.
# Second parameter is the encryption mode . Several encryption mode are available.
des = DES.new(key.encode('utf-8'),DES.MODE_ECB)  # 'utf-8' encode the string to bytes.As Des require the byte as parameter.

# This encrypt function is uesed to encrypt the message.
decrypted_text = des.decrypt(encrypted_text)

print("The Decrypted text is :",decrypted_text.decode())
