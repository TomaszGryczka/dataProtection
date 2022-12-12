from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

client = Client("http://127.0.0.1:5000")

# WSTĘP
client.send_text_message("gryczkat", "wiadomo")

# PIERWSZE ZADANIE
key = RSA.importKey(client.get_key("deadbeef"))
cipher = PKCS1_OAEP.new(key)
encrypted = cipher.encrypt(b"tak")

client.send_binary_message("deadbeef", encrypted)