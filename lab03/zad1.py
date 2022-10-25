from math import log2, ceil

# maksymalna entropia dla klucza AES:
# 256 możliwych znaków
# 32 bajty - długość klucza
aes_key_entropy = 32 * log2(256)

# entropia hasła
# 26 - długość alfabetu bez polskich znaków
# k - długość hasła
# k * log2(26)

# entropia hasła większa lub równa entropii klucza AES
# k * log2(26) >= 32 * log2(256)
# k >= 32 * log2(256) / log2(26)

k = ceil(32 * log2(256) / log2(26))

print("Minimalna długość hasła: ", k)
