import sqlite3
from cryptography.fernet import Fernet
from tkinter import messagebox
import json


with open("config.json") as file:
    config = json.load(file)

    
T = 0

conn = sqlite3.connect("auth.db")
cursor = conn.cursor()

key = config["key"]

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

UNS = []
PWS = []

for row in results:
    def decryptPass(password, key):
        f = Fernet(key)
        decryptPass = f.decrypt(row[2]).decode()
        return decryptPass
    decryptedPass = decryptPass(row[2], key)
    #print(decryptedPass)
    PW_LIST = decryptedPass.split("/n")
    PWS.extend(PW_LIST)
    UN_LIST = row[1].split("/n")
    UNS.extend(UN_LIST)


def login(username, password):
    if username in UNS:
        if password in PWS:
            #messagebox.showinfo("Login", "Login successful!")
            global T
            T = 1
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")        
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")
        

        
conn.close()
