

"""
Implementation of Hill Cipher!

Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)

C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used

"""

from egcd import egcd
import numpy as np
# key is represented into 3*3 matrix
key = np.array([
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
])

"""We find the matrix modulus inverse by
   Step 1) Find determinant
   Step 2) Find determinant value in a specific modulus (usually length of alphabet)
   Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
   """
modulus=26
# Here we calculate the determinant of matrix via np.linalg.det(matrix), since this method calculate the
# result numerically, we need to round off the result to avoid round-off error
det = int(np.round(np.linalg.det(key)))  # Step 1)
# Here we calculate the determinant inverse modulo 26 via extended Euclidean Algorithm
det_inv = pow(det, -1, modulus)
#det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
# Adjoint matrix = determinant * (inverse of matrix)
# Matrix modulo inverse(K^-1) = determinantInverse * Adjoint matrix
matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int) % modulus)  # Step 3)

#key_inv = np.linalg.inv(key)   # invarse matrix

# Input CipherText.
ciphertext = "lnshdlewmtrw"

result=""


i=0
while i < len(ciphertext):
    a = ord(ciphertext[i]) -97
    b = ord(ciphertext[i+1]) - 97
    c = ord(ciphertext[i+2]) - 97
    matrix = np.array([[a],
                       [b],
                       [c]])
    cipher = np.dot(matrix_modulus_inv, matrix)%26      # matrix multiplication
    list = cipher.flatten().tolist()     # convert matrix into list
    for j in range(3):
        result += chr(list[j]+97)
    i = i+3

print("Ciphertext is: ",ciphertext)
print("plaintext is: ",result)








