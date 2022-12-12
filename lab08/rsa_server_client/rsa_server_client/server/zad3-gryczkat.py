from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

client = Client("http://127.0.0.1:5000")

# gryczkat pub file
gryczkat_pub_key_file = open("id_rsa.pub", "rb")
gryczkat_pub_key = gryczkat_pub_key_file.read()

# gryczkat priv file
gryczkat_priv_key_file = open("id_rsa", "rb")
gryczkat_priv_key = gryczkat_priv_key_file.read()
imported_gryczkat_priv_key = RSA.import_key(gryczkat_priv_key)

client.send_key("gryczkat", gryczkat_pub_key)

cipher = PKCS1_OAEP.new(imported_gryczkat_priv_key)

msg = "Hello world!"
encrypted_msg = cipher.encrypt(msg.encode())

hash = SHA256.new(msg.encode())
encrypted_msg_with_sign = pkcs1_15.new(imported_gryczkat_priv_key).sign(hash) + b"<---- HASH | MSG ---->" + encrypted_msg
client.send_binary_message("gryczkat", encrypted_msg_with_sign)