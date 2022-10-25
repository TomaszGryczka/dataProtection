# różnice:

# ECB - ponieważ szyfruje on na podstawie samego klucza, to w trakcie przeglądu zaszyfrowanego 
# obrazu jesteśmy w stanie zobaczyć regularność i domyśleć się kształu oryginalnego obrazu

# CBC nie ma takiego defektu - podczas szyfrowania używa poprzednich bloków, więc każdy kolejny
# blok jest zaszyfrowany w inny sposób

from BMPcrypt import encrypt_data

encrypt_data("demo24.bmp", "CBC", b"abcdefghijklmnop")
encrypt_data("demo24.bmp", "ECB", b"abcdefghijklmnop")

