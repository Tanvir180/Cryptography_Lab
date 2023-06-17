# A python program for rail fence cipher Encryption.


input = open("input.txt", "r+")
output = open("output.txt", "r+")

plaintext = input.read();
ciphertext = ""
depth = 3

cycle = 2 * depth - 2

for row in range(depth):
    index = 0

    # This is for the first rail fence.
    if row == 0:
        while index < len(plaintext):
            ciphertext += plaintext[index]
            index += cycle
    # This is for the last rail fence.
    elif row == (depth - 1):
        index = row
        while index < len(plaintext):
            ciphertext += plaintext[index]
            index += cycle
    # This is for the middel rail fence.
    else:
        left_index = row
        right_index = cycle - row

        while left_index < len(plaintext):
            ciphertext += plaintext[left_index]

            if right_index < len(plaintext):
                ciphertext += plaintext[right_index]

            # Updating the index value.
            left_index += cycle
            right_index += cycle

print(ciphertext)

# Write the ciphertext to the output file.
input.truncate(0)
output.write(ciphertext)

# Close the prviously open file.
input.close()
output.close()
