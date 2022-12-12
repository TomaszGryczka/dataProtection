from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

client = Client("http://127.0.0.1:5000")

gryczkat_pub_key = RSA.import_key(client.get_key("gryczkat"))
cipher = PKCS1_OAEP.new(gryczkat_pub_key)

signed_encrypted_msg = client.get_binary_message("gryczkat")

encrypted_msg = signed_encrypted_msg.split(b"<---- HASH | MSG ---->")[1]
signature = signed_encrypted_msg.split(b"<---- HASH | MSG ---->")[0]

# decrypted_msg = cipher.decrypt(encrypted_msg)
hash_of_decrypted_msg = SHA256.new(encrypted_msg)
print(pkcs1_15.new(gryczkat_pub_key).verify(hash, signature))
