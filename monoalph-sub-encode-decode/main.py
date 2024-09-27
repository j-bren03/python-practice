from functions import *

# Alphabet key, index is the letter value
key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

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