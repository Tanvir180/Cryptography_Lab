print(pow(6, -1, 1))

from sympy import randprime
import random
import math

# Generate two random prime numbers
prime1 = randprime(2, 10**2)  # Adjust the range as needed
prime2 = randprime(2, 10**2)  # Adjust the range as needed
print(prime1)
print(prime2)

n=prime1*prime2
phin = (prime1-1)*(prime2-2)
print(n)
print(phin)

# Generating the public key
e=randprime(1,phin)
while(math.gcd(phin,e)!=1):
  e=random.randint(1,phin)
print(e)


# Generating the private key.
d = pow(e, -1, phin)

plaintext="Tanvir Ahammed Hridoy"

#Encryption Algorithm
i=0
ciphertext=""
length=len(plaintext)
while(i < length):
  value= ord(plaintext[i])
  num= pow(value,e)%n
  ciphertext += chr(num)
  i+=1
print(ciphertext)

#Decryption Algorithm
i=0
plaintext=""
length=len(ciphertext)
while(i < length):
  value= ord(ciphertext[i])
  num= pow(value,d)%n
  plaintext += chr(num)
  i+=1
print(plaintext)
