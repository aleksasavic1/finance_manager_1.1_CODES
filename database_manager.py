import tkinter as tk
from tkinter import messagebox
import json
import sqlite3
from cryptography.fernet import Fernet
import os
import db_info

#print("If you want to view the entire table, press 1. If you want to delete a \
#user from the table, press 2. If you want to exit this program, press ESC.\n")

with open("config.json") as file:
    config = json.load(file)


class database_manager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Database Manager')
        self.iconbitmap('imgs/icon.ico')
        self.minsize(640,480)
        self.resizable(False,False)

        

        self.configure(bg="#0C0908")
        

        #show_users
        self.show_users_button = tk.Button(self, text="SHOW USERS", bg="green", fg="white", command=self.show_users)
        self.show_users_button.pack(pady=20)

        self.show_users_label = tk.Label(self, bg="#0C0908", fg="white", text="User(s):")
        self.show_users_label.pack()
        
        self.text = tk.Text(self, bg="#0C0B0B", fg="white", height=10, width=50)
        self.text.pack()




        #user_id
        self.user_id_label = tk.Label(self, text="UserID:", bg="#0C0908", fg="white")
        self.user_id_input = tk.Entry(self)
        self.user_id_label.place(y=298, x=300)
        self.user_id_input.place(y=320, x=260)


        #password
        self.password_label = tk.Label(self, text="Password:", bg="#0C0908", fg="white")
        self.password_input = tk.Entry(self, show="*")
        self.password_label.place(y=344, x=292)
        self.password_input.place(y=366, x=260)



        #del_user
        self.del_users_button = tk.Button(self, text="DELETE USER", bg="red", fg="white", command=self.del_user)
        self.del_users_button.place(y=404, x=282)




        #exit_button
        def exit_button():
            exit()
        exit_button = tk.Button(self, text='EXIT', command=exit_button, bg="red", fg="white")
        exit_button.place(y=448, x=600)



    #show_users
    def show_users(self):
        conn = sqlite3.connect("auth.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()

        self.text.delete(1.0, tk.END)
        if len(results) == 0:
            messagebox.showinfo("message", "Database is empty.")
        else:
            for row in results:
                self.text.insert(tk.END, f"ID: {row[0]}\nUSERNAME: {row[1]}\n\
PASSWORD: {row[2]}\n")
        conn.close()


    #del_user
    def del_user(self):
        user_id = self.user_id_input.get()
        password = self.password_input.get()
        db_info.userToDelete(user_id, password)
        

        


if __name__ == "__main__":
    dbManager = database_manager()
    dbManager.mainloop()

