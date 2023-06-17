# A python program for rail fence cipher decryption.


input = open("output.txt", "r+")
output = open("input.txt", "r+")

ciphertext = input.read()
depth = 3
cycle = 2 * depth - 2
length = len(ciphertext)

# This makes the plaintext length as the same length of ciphertext.
plaintext = "." * length

# Integer division gives the result same as(Math.floor()).
units = length // cycle

# Make a list of size equal to key.
rails_length = [0] * depth

# Top Rail Length.
rails_length[0] = units

# Intermediate Rail Length.
for i in range(1, depth - 1):
    rails_length[i] = 2 * units
# Bottom Rail Length.
rails_length[depth - 1] = units

# If the length of the ciphertext is not completely divisable by cycle then
# This loop work.
for i in range(length % cycle):
    if i < depth:
        rails_length[i] += 1
    else:
        rails_length[cycle - i] += 1

# Replace the character of the top rail fence into the plaintext.
index = 0
rail_offset = 0
for c in ciphertext[:rails_length[0]]:
    plaintext = plaintext[:index] + c + plaintext[index + 1:]
    index += cycle
rail_offset += rails_length[0]

# Replace the character of the intermediate rail fence into the plaintext.
# As intermediate has two character in each cycle so we need two pointer to indicate them.
for row in range(1, (depth - 1)):
    left_index = row
    right_index = cycle - row
    left_char = True
    for c in ciphertext[rail_offset:rail_offset + rails_length[row]]:
        if left_char:
            plaintext = plaintext[:left_index] + c + plaintext[left_index + 1:]
            left_index += cycle
            left_char = not left_char
        else:
            plaintext = plaintext[:right_index] + c + plaintext[right_index + 1:]
            right_index += cycle
            left_char = not left_char

    # Updating the rail offset value.
    rail_offset += rails_length[row]

# Replace the charater of the bottom rail fence into the plaintext.
index = depth-1
for c in ciphertext[rail_offset:]:
    plaintext = plaintext[:index] + c + plaintext[index + 1:]
    index += cycle

print(plaintext)

# write the plaintext to the output file.
output.write(plaintext)
input.truncate(0)

# Close the previously open file.
input.close()
output.close()