from client import Client
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

client = Client("http://127.0.0.1:5000")

## KEYS
# noname pub file
noname_pub_key_file = open("./keys/id_rsa_noname.pub", "rb")
noname_pub_key = noname_pub_key_file.read()
# noname priv file
noname_priv_key_file = open("./keys/id_rsa_noname", "rb")
noname_priv_key = noname_priv_key_file.read()
imported_noname_priv_key = RSA.import_key(noname_priv_key)
# gryczkat pub file
gryczkat_pub_key = RSA.import_key(client.get_key("gryczkat"))


## SEND SIGNED MESSAGE
# send noname key to server
client.send_key("noname", noname_pub_key)
# encrypting msg with noname public key
msg = "Hello world for NONAME!" 
cipher = PKCS1_OAEP.new(RSA.import_key(client.get_key('gryczkat')))
encrypted_msg = cipher.encrypt(msg.encode())
# add hash to binary msg and send it
hash = SHA256.new(msg.encode())
encrypted_msg_with_sign = pkcs1_15.new(imported_noname_priv_key).sign(hash) + b"<---- HASH | MSG ---->" + encrypted_msg
client.send_binary_message("noname", encrypted_msg_with_sign)

## READ SIGNED GRYCZKAT MESSAGE
cipher = PKCS1_OAEP.new(imported_noname_priv_key)
signed_encrypted_msg = client.get_binary_message("gryczkat")

encrypted_msg = signed_encrypted_msg.split(b"<---- HASH | MSG ---->")[1]
signature = signed_encrypted_msg.split(b"<---- HASH | MSG ---->")[0]

decrypted_msg = cipher.decrypt(encrypted_msg)
hash_of_decrypted_msg = SHA256.new(decrypted_msg)

# verify signature
try:
    pkcs1_15.new(gryczkat_pub_key).verify(hash_of_decrypted_msg, signature)
    print("Wiadomość podpisana prawidłowo")
    print("Wiadomość: ", decrypted_msg)
except:
    print("Wiadomość ze złym podpisem")
    print("Wiadomość: ", decrypted_msg)