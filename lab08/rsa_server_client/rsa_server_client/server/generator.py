from Crypto.PublicKey import RSA

rsa_keys = RSA.generate(2048)

pub_key = rsa_keys.public_key().export_key()
priv_key = rsa_keys.export_key()

pub_key_file = open("./keys/id_rsa_noname.pub", "wb")
priv_key_file = open("./keys/id_rsa_noname", "wb")

pub_key_file.write(pub_key)
priv_key_file.write(priv_key)

rsa_keys = RSA.generate(2048)

pub_key = rsa_keys.public_key().export_key()
priv_key = rsa_keys.export_key()

pub_key_file = open("./keys/id_rsa_gryczkat.pub", "wb")
priv_key_file = open("./keys/id_rsa_gryczkat", "wb")

pub_key_file.write(pub_key)
priv_key_file.write(priv_key)