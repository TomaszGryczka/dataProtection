from math import log2
from Cryptodome.Cipher import ARC4

ARC4.key_size = range(3, 257)

encrypted_file = open("crypto2.rc4", "rb")
encrypted_text = encrypted_file.read()

def shannon_entropy(string):
    entropy = 0.0
    size = len(string)
    for i in range(256):
        prob = string.count(chr(i))/size
        if prob > 0.0:
            entropy += prob * log2(prob)
    return -entropy

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            key = chr(i)+chr(j)+chr(k)
            cipher = ARC4.new(key.encode())
            text = cipher.decrypt(encrypted_text)
            entropy = shannon_entropy(text.decode('latin-1'))
            if entropy < 5:
                print("Entropy value: ", entropy)
                print(text)
                break
