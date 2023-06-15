import random
import string


def generate_login_id(length=8):
    letters = string.ascii_lowercase
    digits = string.digits
    return ''.join(random.choice(letters + digits) for i in range(length))


def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    return ''.join(random.choice(letters + digits + symbols) for i in range(length))


login_id = generate_login_id()
password = generate_password()

print("Login ID:", login_id)
print("Password:", password)