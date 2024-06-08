import sqlite3
from cryptography.fernet import Fernet
from tkinter import messagebox
import json


with open("config.json") as file:
    config = json.load(file)


def register(username, password):
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, \
username TEXT NOT NULL UNIQUE, password TEXT NOT NULL);")
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    UNS = []
    for row in results:
        UN_LIST = row[1].split("\n")
        UNS.extend(UN_LIST)

    if len(username) == 0:
        messagebox.showerror("Registration Error", "The username field cannot be empty.")
    else:
        if username in UNS:
            messagebox.showerror("Registration Error", "Username already exists.")
        else:
            if len(password) >= 8:
                if any(i.isdigit() for i in password):
                    if any(i in "@#$%" for i in password):

                        def encryptPass(password, key):
                            f = Fernet(key)
                            encryptPass = f.encrypt(password.encode())
                            return encryptPass

                        key = config["key"]

                        encryptedPass = encryptPass(password, key)

                    #for row in results:
                        #UN_LIST = row[1].split("\n")
                        #UNS.extend(UN_LIST)

                    #print(len(username))


                        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, encryptedPass))
                        messagebox.showinfo("Registration Message", "Registration successful!")
                    
                    #messagebox.showerror("Registration Error", "The username field cannot be empty.")


                        conn.commit()
                    else:
                        messagebox.showerror("error", "The password must contain at least one of the following special characters: @, #, $ or %")
                else:
                    messagebox.showerror("error", "The password must contain at least one digit.")
            else:
                messagebox.showerror("error", "The password must be at least 8 characters long.")


