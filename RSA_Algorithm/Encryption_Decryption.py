# #print(pow(6, -1, 1))
#
# from sympy import randprime
# import random
# import math
#
# # Generate two random prime numbers
# prime1 = randprime(2, 10**2)  # Adjust the range as needed
# prime2 = randprime(2, 10**2)  # Adjust the range as needed
# print(prime1)
# print(prime2)
#
# n=prime1*prime2
# phin = (prime1-1)*(prime2-2)
# print(n)
# print(phin)
#
# # Generating the public key
# e=randprime(1,phin)
# while(math.gcd(phin,e)!=1):
#   e=random.randint(1,phin)
# print(e)
#
#
# # Generating the private key.
# d = pow(e, -1, phin)
#
# plaintext="Tanvir Ahammed Hridoy"
#
# #Encryption Algorithm
# i=0
# ciphertext=""
# length=len(plaintext)
# while(i < length):
#   value= ord(plaintext[i])
#   num= pow(value,e)%n
#   ciphertext += chr(num)
#   i+=1
# print(ciphertext)
#
# #Decryption Algorithm
# i=0
# plaintext=""
# length=len(ciphertext)
# while(i < length):
#   value= ord(ciphertext[i])
#   num= pow(value,d)%n
#   plaintext += chr(num)
#   i+=1
# print(plaintext)


from sympy import randprime
import random
import math

# Generate two random prime numbers
p = randprime(2, 10**2)  # Adjust the range as needed prime1

q = randprime(2, 10**2)  # Adjust the range as needed prime2
print("prime 1 p = ",p)
print("prime 2 q = ",q)

n=int(p*q)
phin = (p-1)*(q-1)
print("now n = ",n)
print("and phi(n) = " ,phin)

# Generating the public key gcd 1 means break
e=randprime(1,phin)
while(math.gcd(phin,e)!=1):
    e=int(random.randint(1,phin))
print("Public key e = ",e)

# Generating the private key. e and d is inverse modulo phi(n)
d = int(pow(e, -1, phin))
print("Private key d = ",d)
# Message to be encrypted
msg = int(input("Enter the plaintext : "))

# Encryption c = (msg ^ e) % n
c = pow(msg, e, n)
print("Ciphertext = ", c)

# Decryption m = (c ^ d) % n
m = pow(c, d, n)
print("Plaintext = ", m)