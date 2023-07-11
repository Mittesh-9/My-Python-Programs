import argparse
import hashlib

# Parsing
parser = argparse.ArgumentParser(description = "Hashing given passwords")
parser.add_argument("password", help = "input password you want to hash")
parser.add_argument("-t", "--type", default = "sha256", choices = ["sha256", "sha512", "md5"])
args = parser.parse_args()

# Hashing given password
password = args.password
hashtype = args.type
m = getattr(hashlib,hashtype)()
m.update(password.encode())

# Output
print("< hash-type : " + hashtype + " >")
print(m.hexdigest())