import base64
from passlib.hash import argon2

dollar_sign = "$"
equal_sign = "="

checksum = "$argon2id$v=19$m=65536,t=3,p=4$4Vzr3bvXWuvdmzMG4PxfCw$NWNunMWdo0ugkWWsL8Z+sdMKnDcJp0vDfMkr30Lmpd4"
hash_params = checksum.split(dollar_sign)[1:]

hash_salt = base64.b64decode(hash_params[3].encode() + b'==')
argon2_mtp_params = hash_params[2].split(",")
memory_cost = argon2_mtp_params[0].split(equal_sign)[1]
time_cost = argon2_mtp_params[1].split(equal_sign)[1]
parallelism = argon2_mtp_params[2].split(equal_sign)[1]

for i in range(97, 123):
    for j in range(97, 123):
        password = chr(i) + chr(j)
        hash = argon2.using(memory_cost=memory_cost, time_cost=time_cost, parallelism=parallelism, salt=hash_salt).hash(password)
        if(hash == checksum):
            print("Znaleziono hasło: " + password)
            break 
