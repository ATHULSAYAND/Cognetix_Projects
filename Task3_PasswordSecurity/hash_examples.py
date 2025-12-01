import bcrypt

password = b"S3cur3P@ssw0rd!"

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("Password:", password.decode())
print("Salt:", salt.decode())
print("Hashed:", hashed.decode())

verify = bcrypt.checkpw(password, hashed)
print("Match:", verify)
