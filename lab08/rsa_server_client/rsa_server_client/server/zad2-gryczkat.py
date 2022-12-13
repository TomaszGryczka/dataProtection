from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

client = Client("http://127.0.0.1:5000")

# gryczkat pub file
gryczkat_pub_key_file = open("./keys/id_rsa_gryczkat.pub", "rb")
gryczkat_pub_key = gryczkat_pub_key_file.read()

# gryczkat priv file
gryczkat_priv_key_file = open("./keys/id_rsa_gryczkat", "rb")
gryczkat_priv_key = gryczkat_priv_key_file.read()
imported_gryczkat_priv_key = RSA.import_key(gryczkat_priv_key)

client.send_key("gryczkat", gryczkat_pub_key)


## READING MESSAGE
cipher = PKCS1_OAEP.new(imported_gryczkat_priv_key)
encrypted_msg = client.get_binary_message("gryczkat")
msg = cipher.decrypt(encrypted_msg)
print(msg)

## SENDING MESSAGE
noname_pub_key = RSA.import_key(client.get_key("noname"))

cipher = PKCS1_OAEP.new(noname_pub_key)

msg = b"MESSAGE FOR NONAME"
encrypted_msg = cipher.encrypt(msg)
client.send_binary_message("noname", encrypted_msg)