import sys
import os 
from password_encrypter import encrypt_password, decrypt_password


def write_login_and_password_to_file(path, login, password):
    try:
        file = open(path, "w+")
        hashed, verified = encrypt_password(password)
        if verified:
            file.write("Login: " + login + "\nPassword: " + password)
            print("hashed password:" + hashed)
        else:
            print("couldn't hash the password")
        file.close()
    except FileNotFoundError:
        "unable to create a file"
        sys.exit(2)


def read_login_and_password_from_file(path):
    if os.path.exists(path):
        file = open(path, "r")
        content = file.read().split()
        login = content[1]
        password = encrypt_password(content[3])
        return login, password