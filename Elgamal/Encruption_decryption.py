# # Sympy is a Python library for symbolic mathematics.
# from sympy import primitive_root, randprime
# import random
#
# # The number for which you want to find the primitive root
# prime = randprime(124,10**3)
# root = primitive_root(prime)
#
# d=random.randint(1,(prime-2)) # It is private key.
#
# e=(pow(root,d)%prime)  # It is public key.
# r=random.randint(1,10)  # Select a random integer.
#
# #Define the plaintext.
# plaintext = "Tanvir Ahammed Hridoy"
#
# # Encryption Algorithm.
# ciphertext=[]
# for char in plaintext:
#   ciphertext1=(pow(root,r)%prime)
#   ciphertext2=((ord(char)*pow(e,r))%prime)
#   ciphertext.append((ciphertext1,ciphertext2))
# print(ciphertext)
#
#
# #Decryption Algorithm
# plaintext=""
# for pair in ciphertext:
#   ciphertext1,ciphertext2=pair
#   value=pow(ciphertext1,d)
#   multinv = pow(value,-1,prime)
#   decrypt_char = (ciphertext2*multinv) % prime
#   plaintext += chr(decrypt_char)
# print(plaintext)
#
from sympy import primitive_root, randprime
import random


# The number for which you want to find the primitive root
p = randprime(2,10**3)
print("Prime p = ",p)
e1 = primitive_root(p)
print("Primitive root e1 = ",e1)

d=random.randint(1,(p-2)) # It is private key. (1<=d<p-2)
print("Private key d = ",d)
e2=(pow(e1,d)%p)  # It is public key.
print("public key e2 = ",e2)

r=random.randint(1,10)  # Select a random integer.
print("Random number r = ",r)
#Define the plaintext.
plaintext = int(input("\nEnter the plaintext : "))

# Encryption Algorithm.
ciphertext=""
ciphertext1=pow(e1,r,p)
ciphertext2=((plaintext*pow(e2,r))%p)
print("ciphertext is = ",ciphertext1," , ",ciphertext2)

#Decryption Algorithm
plaintext =""
value=pow(ciphertext1,d)
multinv = pow(value,-1,p)
plaintext = (ciphertext2*multinv) % p
print("plaintext is = ",plaintext)