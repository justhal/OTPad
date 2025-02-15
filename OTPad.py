plaintext = "Hi"
key = "SK"

ciphertext = ""

for index in range(len(plaintext)):
    plaintext_character = plaintext[index]
    key_character = key[index]
    plaintext_integer = ord(plaintext_character)
    key_integer = ord(key_character)
    ciphertext_integer = plaintext_integer ^ key_integer
    ciphertext_character = chr(ciphertext_integer)
    ciphertext = ciphertext_character + ciphertext 

print(ciphertext)

# XOR Operation:
# Plaintext 7   0111
# Key 3         0011
# ------------------
# Ciphertext    0100



