import sqlite3
from cryptography.fernet import Fernet
from tkinter import messagebox
import json
import os

with open("config.json") as file:
    config = json.load(file)

key = config["key"]


conn = sqlite3.connect("auth.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()


ID = []
PW = []

for row in results:
    ID_LIST = [row[0]]
    ID.extend(ID_LIST)
    
    def decryptPass(password, key):
        f = Fernet(key)
        decryptPass = f.decrypt(row[2]).decode()
        return decryptPass
    decryptedPass = decryptPass(row[2], key)
    #print(decryptedPass)
    PW_LIST = decryptedPass.split("\n")
    PW.extend(PW_LIST)



def userToDelete(user_id, password):
    conn_ = sqlite3.connect("auth.db")
    cursor_ = conn_.cursor()
    key = config["key"]

    try:
        userToDelete = int(user_id)
    except ValueError:
        messagebox.showerror("error", "Please enter the ID number!")
        return

    cursor_.execute("SELECT id FROM users")
    IDs = cursor_.fetchall()
    user_found = False
    for i in IDs:
        if userToDelete in i:
            user_found = True
    if user_found:
        try:
            userPWD = password
            cursor_.execute("SELECT password FROM users WHERE id = ?", (userToDelete,))
            pwd_result = cursor_.fetchall()
            PWD = pwd_result[0][0]
            def decryptPass(password, key):
                f = Fernet(key)
                decryptPass = f.decrypt(PWD).decode()
                return decryptPass
            decryptedPass = decryptPass(PWD, key)
            if decryptedPass == userPWD:
                cursor_.execute("SELECT username FROM users WHERE id = ?", (userToDelete,))
                result_ = cursor_.fetchall()
                username = result_[0][0]
                txtName = f"{username}.txt"
                if os.path.exists(f"users/{txtName}"):
                    os.remove(f"users/{txtName}")
                cursor_.execute("DELETE FROM users WHERE id = ?", (userToDelete,))
                conn_.commit()
                messagebox.showinfo("message", f"User {username} has been successfully deleted.")
            else:
                messagebox.showerror("error", "You have entered the wrong password.")
        except ValueError:
            messagebox.showerror("error", "Please enter a number.")
    else:
        messagebox.showerror("error", "User is not found.")

#userToDelete(1, 'a1')
#userToDelete(1, 'a2')
#userToDelete(2, 'a1')    

conn.close()
