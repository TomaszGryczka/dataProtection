from base64 import decode, encode
from operator import mod
from Cryptodome.Cipher import ARC4

ARC4.key_size = range(3, 257)

text = "Lorem ipsum dolores"
key = "Key"

def prepare_permutation(key):
    d = len(key)
    S = [0] * 256

    for i in range(256):
        S[i] = i

    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % d])) % 256
        S[j], S[i] = S[i], S[j]
    
    return S


def arc4_encode(key, data):
    encoded_data = ""
    data_size_in_bytes = len(data)
    
    S = prepare_permutation(key)

    i = 0
    j = 0
    m = 0
    while m < data_size_in_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[j], S[i] = S[i], S[j]
        encoding_byte = S[(S[i] + S[j]) % 256]
        encoded_data += str(hex(ord(data[m]) ^ encoding_byte)) + " "
        m = m + 1

    return encoded_data

def arc4_decode(key, data):
    splittedData = data.split()
    decoded_data = ""
    data_size_in_bytes = len(splittedData)
    
    S = prepare_permutation(key)

    i = 0
    j = 0
    m = 0
    while m < data_size_in_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[j], S[i] = S[i], S[j]
        encoding_byte = S[(S[i] + S[j]) % 256]
        decoded_data += str(chr(int(splittedData[m], 16) ^ encoding_byte))
        m = m + 1

    return decoded_data

encoded = arc4_encode(key, text)
decoded = arc4_decode(key, encoded)

print("Zaszyfrowane własnym algorytmem + odszyfrowanie:")
print(encoded)
print(decoded)


cip = ARC4.new(key.encode())
encrypted = cip.encrypt(text.encode())
cip = ARC4.new(key.encode())
decrypted = cip.encrypt(encrypted)

print("Zaszyfrowanie algorytmem z biblioteki + odszyfrowanie")
print(encrypted)
print(decrypted)