from Crypto.PublicKey import RSA

rsa_keys = RSA.generate(2048)

pub_key = rsa_keys.public_key().export_key()
priv_key = rsa_keys.export_key()

pub_key_file = open("id_rsa.pub", "wb")
priv_key_file = open("id_rsa", "wb")

pub_key_file.write(pub_key)
priv_key_file.write(priv_key)