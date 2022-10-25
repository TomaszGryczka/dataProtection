from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import itertools as it

BLOCK_SIZE = 16

encrypted_bmp_file = open("security_ECB_encrypted.bmp","rb").read()
padded_encrypted_bmp_file = pad(encrypted_bmp_file, BLOCK_SIZE)

for i in it.chain(range(48, 58), range(97, 123)):
    password = chr(i) * 16

    cipher = AES.new(password.encode(), AES.MODE_ECB)
    decrypted_file = cipher.decrypt(padded_encrypted_bmp_file)
    decoded_decrypted_file = decrypted_file.decode("latin1")

    file = open('decrypted.bmp', 'wb')
    if decoded_decrypted_file.find("BM") == 0:
        file.write(decrypted_file)
        file.close()

        print("Złamane hasło: ", password)
        print("Zapisany rozszyfrowany plik: decrypted.bmp")

        break