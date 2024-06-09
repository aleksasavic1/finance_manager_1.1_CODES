import tkinter as tk
from tkinter import messagebox
import register
import login
import fmApp
import sqlite3
import os
import sys



try:
    os.mkdir("users")
except FileExistsError:
    pass

def run_again():
    python = sys.executable
    os.execl(python, python, *sys.argv)


conn = sqlite3.connect('auth.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

UNS = []

for row in results:
    UN_LIST = row[1].split("\n")
    UNS.extend(UN_LIST)


class FinanceManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Finance Manager 1.1')
        self.iconbitmap("imgs/icon.ico")
        self.minsize(640,480)
        self.resizable(False,False)



        #bg       
        bgImage = tk.PhotoImage(file="imgs/background_image.png")
        bg_label = tk.Label(image=bgImage)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)
        bg_label.image = bgImage
        
        
   

        # LOGIN
        self.loginFrame = tk.Frame(self)
        self.loginFrame.pack(pady=46)
        
        self.username_label = tk.Label(self, text="Username:", bg="#42b4e6")
        self.username_input = tk.Entry(self, bg="#EBEBEB")
        self.password_label = tk.Label(self, text="Password:", bg="#42b4e6")
        self.password_input = tk.Entry(self, bg="#EBEBEB", show="*")
        self.login_button = tk.Button(self, text="Login", bg="#CBD6E2", command=self.login)

        self.username_label.pack()
        self.username_input.pack()
        self.password_label.pack()
        self.password_input.pack()
        self.login_button.pack(pady=8)

        # REGISTER
        self.registerFrame = tk.Frame(self)
        self.registerFrame.pack(pady=24)
        
        self.r_username_label = tk.Label(self, text="Username:", bg="#42b4e6")
        self.r_username_input = tk.Entry(self, bg="#EBEBEB")
        self.r_password_label = tk.Label(self, text="Password:", bg="#42b4e6")
        self.r_password_input = tk.Entry(self, bg="#EBEBEB", show="*")
        self.register_button = tk.Button(self, text="Register", bg="#CBD6E2", command=self.register)

        self.r_username_label.pack()
        self.r_username_input.pack()
        self.r_password_label.pack()
        self.r_password_input.pack()
        self.register_button.pack(pady=8)

        #created by
        self.created_by = tk.Label(self, bg="#42b4e6", text="Created by Aleksa Savic")
        self.created_by.place(y=458, x=4)



        #exit_button
        def exit_button():
            exit()
        exit_button = tk.Button(self, text='EXIT', command=exit_button, bg="red", fg="white")
        exit_button.place(x=598, y=444)

    def login(self):
        self.username = self.username_input.get()
        password = self.password_input.get()
        login.login(self.username,password)
        if login.T == 1:
            self.destroy()
            self.AppScreen()
        
    def AppScreen(self):
        #current_budget
        filePath = f"users/{self.username}.txt"

        if os.path.exists(filePath):
            with open(filePath, "r") as file:
                UPD = file.read()
                fmApp.current_budget(self.username, UPD)
        else:
            fmApp.current_budget(self.username, "0")
        
        
        def currentBudget():
            global current_budget
            current_budget = current_budget_input.get()
        def sendCurrentBudget():
            value = current_budget_input.get()
            try:
                value_int = int(value)
                fmApp.current_budget(self.username, value)
                sent_label.config(text="Sent!")
            except ValueError:
                sent_label.config(text="Must be a number!")
                

        #add_budget
        def addBudget():
            global add_budget
            add_budget = add_budget_input.get()
        def sendAddedBudget():
            value = add_budget_input.get()
            try:
                value_int = int(value)
                fmApp.add_budget(self.username, value)
                added_label.config(text="Added!")
            except ValueError:
                added_label.config(text="Must be a number!")

        #subtract_budget
        def subtractBudget():
            global subtract_budget
            subtract_budget = subtract_budget_input.get()
        def sendSubtractedBudget():
            value = subtract_budget_input.get()
            try:
                value_int = int(value)
                fmApp.subtract_budget(self.username, value)
                subtracted_label.config(text="Subtracted!")
            except ValueError:
                subtracted_label.config(text="Must be a number!")

        #view_balance
        def viewBalance():
            global UNS
            if self.username in UNS:
                with open(f'users/{self.username}.txt', 'r') as file:
                    balance = file.read()
                    balanceTEXT.config(state=tk.NORMAL)
                    balanceTEXT.delete("1.0", tk.END)
                    balanceTEXT.insert(tk.END, balance)
                    balanceTEXT.config(state=tk.DISABLED)
                root.after(1000, viewBalance)
            
            
        
        root = tk.Tk()
        root.title('Finance Manager 1.1')
        root.iconbitmap("imgs/icon.ico")
        root.minsize(640,480)
        root.resizable(False,False)


        #bg_for_app
        bgAppImage = tk.PhotoImage(file="imgs/background_image.png")
        bgApp_label = tk.Label(image=bgAppImage)
        bgApp_label.place(x=0,y=0,relwidth=1,relheight=1)
        bgApp_label.image = bgAppImage
        

        
        current_budget = None
        add_budget = None
        subtract_budget = None
        
        #current_budget
        current_budget_label = tk.Label(text='CURRENT BUDGET', bg="#42b4e6")
        current_budget_input = tk.Entry(root, bg="#EBEBEB")
        current_budget_button = tk.Button(root, text='SEND', bg="#D8F9FF", command=sendCurrentBudget)
        

        current_budget_label.pack()
        current_budget_input.pack(pady=6)
        current_budget_button.pack()

        sent_label = tk.Label(root, text="", bg="#42b4e6")
        sent_label.pack()


        #add_budget
        add_budget_label = tk.Label(text='ADD BUDGET', bg="#42b4e6")
        add_budget_input = tk.Entry(root, bg="#EBEBEB")
        add_budget_button = tk.Button(root, text='ADD', bg="#D8F9FF", command=sendAddedBudget)

        add_budget_label.pack()
        add_budget_input.pack(pady=6)
        add_budget_button.pack()

        added_label = tk.Label(root, text="", bg="#42b4e6")
        added_label.pack()


        #subtract_budget
        subtract_budget_label = tk.Label(text='SUBTRACT BUDGET', bg="#42b4e6")
        subtract_budget_input = tk.Entry(root, bg="#EBEBEB")
        subtract_budget_button = tk.Button(root, text='SUBTRACT', bg="#D8F9FF", command=sendSubtractedBudget)

        subtract_budget_label.pack()
        subtract_budget_input.pack(pady=6)
        subtract_budget_button.pack()

        subtracted_label = tk.Label(root, text="", bg="#42b4e6")
        subtracted_label.pack(pady=8)




        #view_balance
        balanceTEXT = tk.Text(root, width=10, height=1)
        balanceTEXT.pack()
        viewBalance()



        #exit_button
        def exit_button():
            exit()
        exit_button = tk.Button(root, text='EXIT', command=exit_button, bg="red", fg="white")
        exit_button.place(x=598, y=444)


        
        root.mainloop()
      

    def register(self):
        r_username = self.r_username_input.get()
        r_password = self.r_password_input.get()
        register.register(r_username, r_password)
        run_again()


if __name__ == "__main__":
    app = FinanceManager()
    app.mainloop()
