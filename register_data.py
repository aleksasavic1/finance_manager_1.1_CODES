from cryptography.fernet import Fernet
import json


with open("config.json") as file:
    config = json.load(file)


def encryptPass(password, key):
    f = Fernet(key)
    encryptPass = f.encrypt(password.encode())
    return encryptPass


key = config["key"]
#print(key)

encryptedPass = encryptPass(password, key)

#print(encryptedPass)
