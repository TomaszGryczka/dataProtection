import string
import random
from passlib.hash import md5_crypt

const_salt = "123"
dollar_sign = "$"

hashes = {}

while(True):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    hash = md5_crypt.hash(random_string, salt=const_salt).split(dollar_sign)[3][:5]
    if(hash in hashes.keys()):
        print("Znaleziono dwa hashe o identycznych pierwszych 5 bajtach sumy kontrolnej:")
        print("Pierwsze pięć bajtów: " + hash)
        print("Pierwszy string:" + random_string)
        print("Drugi string: " + hashes[hash])
        break
    hashes[hash] = random_string

# Przykładowy wynik:
# Znaleziono dwa hashe o identycznych pierwszych 5 bajtach sumy kontrolnej:
# Pierwsze pięć bajtów: SypIB
# Pierwszy string:m2ONXMdRX424y8A5
# Drugi string: cnbcp48HtoIIWK0m