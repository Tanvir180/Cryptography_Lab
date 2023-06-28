import numpy as np
plaintext = "meetmeatthepark"

k=2,0,1,3
key=len(k)
cipher = []
ciphertext = ['']*key

for column in range(key):
    pointer = column

    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]

        pointer += key

#print(ciphertext)
for i in range(key):
    key1=k[i]
    cipher.insert(key1,ciphertext[i])
print("PlainText Is : " +plaintext)
print(ciphertext)

print("After Using key Ciphertext is:  "+''.join(cipher)) #converting list to string

# Decryption
plain = []
i=0
for i in range(key):
    j=k[i]
    plain.insert(i,cipher[j])

print(plain)

pt=""

f=0
for i in range(key):
    for k in plain:
         m = 0
         for j in k:
             if(m==f):
                 pt+=j
             m=m+1
    f=f+1
print("After decryption plaintext:  "+pt)
