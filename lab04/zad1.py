import base64
from passlib.hash import sha512_crypt, sha256_crypt, argon2, sha1_crypt, md5_crypt, bcrypt

password = "password"
dollar_sign = "$"
equal_sign = "="

hashes_file = open("hashes.txt", "r")

# first hash -> sha1
sha1_hash_line = hashes_file.readline()
sha1_hash_params = sha1_hash_line.split(dollar_sign)[1:]
sha1_hash = sha1_crypt.hash(password, salt=sha1_hash_params[2], rounds=sha1_hash_params[1])

# second hash -> sha256
sha256_hash_line = hashes_file.readline()
sha256_hash_params = sha256_hash_line.split(dollar_sign)[1:]
sha256_hash = sha256_crypt.hash(password, salt=sha256_hash_params[2], rounds=sha256_hash_params[1].split(equal_sign)[1])

# third hash -> sha512
sha512_hash_line = hashes_file.readline()
sha512_hash_params = sha512_hash_line.split(dollar_sign)[1:]
sha512_hash = sha512_crypt.hash(password, salt=sha512_hash_params[2], rounds=sha512_hash_params[1].split(equal_sign)[1])

# fourth hash -> bcrypt | 2y identical to 2b
bcrypt_2y_hash_line = hashes_file.readline()
bcrypt_2y_hash_params = bcrypt_2y_hash_line.split(dollar_sign)[1:]
bcrypt_2y_salt = bcrypt_2y_hash_params[2][:22]
bcrypt_2y_hash = bcrypt.hash(password, salt=bcrypt_2y_salt, rounds=bcrypt_2y_hash_params[1], ident="2y")

# fifth hash -> bcrypt | 2b identical to 2y
bcrypt_2b_hash_line = hashes_file.readline()
bcrypt_2b_hash_params = bcrypt_2b_hash_line.split(dollar_sign)[1:]
bcrypt_2b_salt = bcrypt_2b_hash_params[2][:22]
bcrypt_2b_hash = bcrypt.hash(password, salt=bcrypt_2b_salt, rounds=bcrypt_2b_hash_params[1], ident="2b")

# sixth hash -> md5
md5_1_hash_line = hashes_file.readline()
md5_1_hash_params = md5_1_hash_line.split(dollar_sign)[1:]
md5_1_hash = md5_crypt.hash(password, salt=md5_1_hash_params[1])

# seventh hash -> md5
md5_2_hash_line = hashes_file.readline()
md5_2_hash_params = md5_2_hash_line.split(dollar_sign)[1:]
md5_2_hash = md5_crypt.hash(password, salt=md5_2_hash_params[1])

# eighth hash -> argon2
argon2_hash_line = hashes_file.readline()

argon2_hash_params = argon2_hash_line.split(dollar_sign)[1:]

argon2_mtp_params = argon2_hash_params[2].split(",")
memory_cost = argon2_mtp_params[0].split(equal_sign)[1]
time_cost = argon2_mtp_params[1].split(equal_sign)[1]
parallelism = argon2_mtp_params[2].split(equal_sign)[1]

argon2_hash_salt = base64.b64decode(argon2_hash_params[3].encode() + b'==') # incorrect padding error

argon2_hash = argon2.using(memory_cost=memory_cost, time_cost=time_cost, parallelism=parallelism, salt=argon2_hash_salt).hash(password)


# printing result
print("SHA1:")
print("Oryginalny hash:")
print("  " + sha1_hash_line)
print("Odtworzony hash:")
print("  '" + sha1_hash + "'\n\n")

print("SHA256:")
print("Oryginalny hash:")
print("  " + sha256_hash_line)
print("Odtworzony hash:")
print("  '" + sha256_hash + "'\n\n")

print("SHA512:")
print("Oryginalny hash:")
print("  " + sha512_hash_line)
print("Odtworzony hash:")
print("  '" + sha512_hash + "'\n\n")

print("BCRYPT 2Y:")
print("Oryginalny hash:")
print("  " + bcrypt_2y_hash_line)
print("Odtworzony hash:")
print("  '" + bcrypt_2y_hash + "'\n\n")

print("BCRYPT 2B:")
print("Oryginalny hash:")
print("  " + bcrypt_2b_hash_line)
print("Odtworzony hash:")
print("  '" + bcrypt_2b_hash + "'\n\n")

print("MD5:")
print("Oryginalny hash:")
print("  " + md5_1_hash_line)
print("Odtworzony hash:")
print("  '" + md5_1_hash + "'\n\n")

print("MD5:")
print("Oryginalny hash:")
print("  " + md5_2_hash_line)
print("Odtworzony hash:")
print("  '" + md5_2_hash + "'\n\n")

print("ARGON2:")
print("Oryginalny hash:")
print("  " + argon2_hash_line)
print("Odtworzony hash:")
print("  '" + argon2_hash + "'\n\n")
