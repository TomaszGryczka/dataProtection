from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

client = Client("http://127.0.0.1:5000")

gryczkat_pub_key = RSA.import_key(client.get_key("gryczkat"))
print(gryczkat_pub_key)

cipher = PKCS1_OAEP.new(gryczkat_pub_key)

msg = b"Widzisz mnixcvvcxe? Co nie?"
encrypted_msg = cipher.encrypt(msg)
client.send_binary_message("gryczkat", encrypted_msg)