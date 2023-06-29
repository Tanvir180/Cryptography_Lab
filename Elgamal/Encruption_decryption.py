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
