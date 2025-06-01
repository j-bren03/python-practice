from functions import *

# Alphabet key, index is the letter value
key = [chr(char) for char in range(97, 123)]

msg = input("").split()
msg = "".join(msg)

encoded_msg = add_cipher_encode(msg, 3, key)
print(encoded_msg)

decoded_msg = add_cipher_decode(encoded_msg, 3, key)
print(decoded_msg)

msg = input("").split()
msg = "".join(msg)

encoded_msg = mult_cipher_encode(msg, 3, key)
print(encoded_msg)

decoded_msg = mult_cipher_decode(encoded_msg, 4, key)
print(decoded_msg)

msg = input("").split()
msg = "".join(msg)

encoded_msg = affine_cipher_encode(msg, 3, 20, key)
print(encoded_msg)

decoded_msg = affine_cipher_decode(encoded_msg, 3, 20, key)
print(decoded_msg)