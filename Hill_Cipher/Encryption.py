"""
Implementation of Hill Cipher!

Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)

C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used

"""

import numpy as np
# key is represented into 3*3 matrix
key = np.array([
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
])

# Input PlainText.
plaintext = "paymoremoney"

# plaintextpair = []
# ciphertextpair = []
result=""


# dividing plain text into 3 each
#i = 0
# while i < len(plaintext):
#     a = plaintext[i]
#     b = plaintext[i+1]
#     c=plaintext[i+2]
#
#     plaintextpair.append(a + b + c)
#     i += 3

i=0
while i < len(plaintext):
    a = ord(plaintext[i]) -97
    b = ord(plaintext[i+1]) - 97
    c = ord(plaintext[i+2]) - 97
    matrix = np.array([[a],
                       [b],
                       [c]])
    cipher = np.dot(key, matrix)%26      # matrix multiplication
    list = cipher.flatten().tolist()     # convert matrix into list
    for j in range(3):
        result += chr(list[j]+97)
    i = i+3

print("plaintext is: ",plaintext)
print("Ciphertext is: ",result)





