def add_cipher_encode(msg: str, add_key: int, keys: list) -> str:
    # encode formula: y = x + a (mod 26)
    encoded_msg = ""

    for char in msg.lower():
        y = (keys.index(char) + add_key) % 26
        y = keys[y]
        encoded_msg += y

    return encoded_msg.upper()


def add_cipher_decode(msg: str, add_key: int, keys: list) -> str:
    # decode formula: x = y + a^-1 (mod 26)
    decoded_msg = ""
    a_inv = 26 - add_key

    for char in msg.lower():
        x = (keys.index(char) + a_inv) % 26
        x = keys[x]
        decoded_msg += x

    return decoded_msg

def mult_cipher_encode(msg: str, mult_key: int, keys: list) -> str:
    # encode formula: y = mx (mod 26)
    encoded_msg = ""
    
    for char in msg.lower():
        y = (mult_key * keys.index(char)) % 26
        y = keys[y]
        encoded_msg += y

    return encoded_msg.upper()

def mult_cipher_decode(msg: str, mult_key: int, keys: list) -> str:
    # decode formula: x = m^-1*y (mod 26)
    pass

def affine_cipher_encode(msg: str, mult_key: int, add_key: int, keys: list) -> str:
    pass

def affine_cipher_decode(msg: str, mult_key: int, add_key: int, keys: list) -> str:
    pass