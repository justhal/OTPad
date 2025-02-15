plaintext = "Hi"
key = "SK"

ciphertext = ""

#print(ciphertext)

def decrypt(ciphertext, key):
    if len(key) != len(ciphertext):
        raise ValueError
    plaintext = ""
    for c, k in zip(ciphertext, key):
        plaintext += chr(ord(c) ^ ord(k))
    return plaintext

ciphertext = decrypt(plaintext, key)

#decrypted = decrypt(ciphertext, key)

#print(decrypted)

decrypted = ""

for index in range(len(plaintext)):
    plaintext_character = ciphertext[index]
    key_character = key[index]
    plaintext_integer = ord(plaintext_character)
    key_integer = ord(key_character)
    ciphertext_integer = plaintext_integer ^ key_integer
    ciphertext_character = chr(ciphertext_integer)
    decrypted = decrypted + ciphertext_character

print(decrypted)

# XOR Operation:
# Plaintext 7   0111
# Key 3         0011
# ------------------
# Ciphertext    0100

# Plaintext     72      01001000
# Key           83      01010011
# Ciphertext    34      00011011




