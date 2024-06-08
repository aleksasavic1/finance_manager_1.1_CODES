import sqlite3

conn = sqlite3.connect('auth.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

results = cursor.fetchall()

UNS = []

for row in results:
    UN_LIST = row[1].split("/n")
    UNS.extend(UN_LIST)
#print(UNS)

#with open('/users/users.txt', 'w') as file:
    #file.write()


def current_budget(user, price):
    global UNS
    if user in UNS:
        with open(f'users/{user}.txt', 'w') as file:
            file.write(f'{price}')
    #print(UNS)


def add_budget(user, price):
    global UNS
    if user in UNS:
        with open(f'users/{user}.txt', 'r') as file:
            balance = file.read()
            #print(balance)
        with open(f'users/{user}.txt', 'w') as file:
            new_balance = int(balance) + int(price)
            file.write(f'{new_balance}')
            #print(new_balance)


def subtract_budget(user, price):
    global UNS
    if user in UNS:
        with open(f'users/{user}.txt', 'r') as file:
            balance = file.read()
            #print(balance)
        with open(f'users/{user}.txt', 'w') as file:
            new_balance = int(balance) - int(price)
            file.write(f'{new_balance}')
            #print(new_balance)

conn.close()
