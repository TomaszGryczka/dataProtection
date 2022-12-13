from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

client = Client("http://127.0.0.1:5000")

## KEYS
# gryczkat pub file
noname_pub_key_file = open("./keys/id_rsa_noname.pub", "rb")
noname_pub_key = noname_pub_key_file.read()
# noname priv file
noname_priv_key_file = open("./keys/id_rsa_noname", "rb")
noname_priv_key = noname_priv_key_file.read()
imported_noname_priv_key = RSA.import_key(noname_priv_key)
# send noname pub key
client.send_key("noname", noname_pub_key)


## READING MESSAGE
cipher = PKCS1_OAEP.new(imported_noname_priv_key)
encrypted_msg = client.get_binary_message("noname")
msg = cipher.decrypt(encrypted_msg)
print(msg)

## SENDING MESSAGE
gryczkat_pub_key = RSA.import_key(client.get_key("gryczkat"))

cipher = PKCS1_OAEP.new(gryczkat_pub_key)

msg = b"MESSAGE FOR GRYCZKAT"
encrypted_msg = cipher.encrypt(msg)
client.send_binary_message("gryczkat", encrypted_msg)