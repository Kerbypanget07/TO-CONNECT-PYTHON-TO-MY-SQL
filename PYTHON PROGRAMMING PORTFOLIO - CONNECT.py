import time
import re
import hashlib
import datetime
import mysql.connector
import tkinter as tk
from tkinter import *

def ld():
    c = "Now Loading"
    print(c, end="")
    for a in "...":
        time.sleep(0.5)
        print(a, end="")
    print()

def wlc():
    for d in "\nGreetings, Welcome to Kear's Restaurant! ver 1.0":
        time.sleep(0.1)
        print(d, end="")
    print()

def pgm(answer):
    if answer.lower() == "y":
        return "Welcome!"
    elif answer.lower() == "n":
        return "Goodbye."
    else:
        return "Please input Y or N only."

print ()

ld()
time.sleep(1)
wlc()

while True:
    v = "\nWould you like to launch the program? (Y/N)"
    print(v)
    try:
        answer = input("Response: ")
        if answer.lower() == "n":
            print(pgm(answer))
            exit()
        elif answer.lower() == "y":
            break
        else:
            print(pgm(answer))
    except ValueError:
        print("Please enter only letters.")
        exit()

ld()

def signup():
    print("Personal Details: (Sign-In)")

    while True:
        email = input("Provide email address: ")
        match = re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|yahoo|protonmail|outlook|aol|zoho|iCloud|yahoo!|gmx)\.[a-zA-Z]{2,}$", email)

        if match:
            print("Your email is Saved!")
            break

        else:
            print("Access Denied. Please enter another valid email.")

    while True:
        password = input("Enter a strong password (Should be at least 8 characters and numbers): ")
        if len(password) < 8:
            print("Access Denied. Password should be at least 8 characters.")
            continue
        match = re.search(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$', password)

        if match:
            print("Your password is saved!")
            print("Login to Continue")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            f2[email] = hashed_password
            break

        else:
            print("Invalid password. Please enter a valid password.")

def home():
    time.sleep(1)
    print()

    def wlc2():
        for d in "Welcome to Kear's Restaurant Website!\nSharing is Kearing~":
            time.sleep(0.1)
            print(d, end="")
        print()

    wlc2()
    n = datetime.datetime.now()
    time.sleep(1)
    v = ("\nDate and time as of right now:")
    print(v, n)

print()

def dl():
    c = "Launching Application"
    print(c, end="")
    for a in "...":
        time.sleep(0.5)
        print(a, end="")
    print()
dl()

f2 = {}
signup()
home()

def ls():
    loading_window = tk.Tk()

    loading_window.geometry('500x700')

    loading_window.title('Loading')

    loading_label = tk.Label(loading_window, text='Program is Now Loading...', font=('Barlow', 30, 'italic'))
    loading_label.pack(pady=20)

    loading_window.after(3000, loading_window.destroy) # destroy the loading screen after 3 seconds

    loading_window.mainloop()

ls()

# =----------Database----------=
mydb = mysql.connector.connect(
  host="localhost",
  user="kervs",
  password="YES",
  database="restaurant"
)

# =----------Cursor object----------=
mycursor = mydb.cursor()

# =----------Tkinter GUI----------=
root = Tk()
root.title("Kear's Reastaurant")
root.minsize(width=500, height=700)
root.configure(bg="yellow")

def create():
    name = name_entry.get()
    category = category_entry.get()
    price = price_entry.get()
    sql = "INSERT INTO menu (name, category, price) VALUES (%s, %s, %s)"
    val = (name, category, price)
    mycursor.execute(sql, val)
    mydb.commit()
    message.config(text="Record created successfully!")

def read():
    mycursor.execute("SELECT * FROM menu")
    result = mycursor.fetchall()
    for x in result:
        print(x)

def update():
    name = name_entry.get()
    category = category_entry.get()
    price = price_entry.get()
    sql = "UPDATE menu SET category = %s, price = %s WHERE name = %s"
    val = (category, price, name)
    mycursor.execute(sql, val)
    mydb.commit()
    message.config(text="Record updated successfully!")

def delete():
    name = name_entry.get()
    sql = "DELETE FROM menu WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    mydb.commit()
    message.config(text="Record deleted successfully!")

name_label = Label(root, text="Name:", font=("Barlow", 20,"normal"), bg="yellow")
name_label.place(x=0, y=0)
name_entry = Entry(root)
name_entry.place(x=100, y=10)

category_label = Label(root, text="Category:", font=("Barlow", 20,"normal"), bg="yellow")
category_label.place(x=0, y=50)
category_entry = Entry(root)
category_entry.place(x=140, y=60)

price_label = Label(root, text="Price:", font=("Barlow", 20,"normal"), bg="yellow")
price_label.place(x=0, y=100)
price_entry = Entry(root)
price_entry.place(x=100, y=110)

message = Label(root, text="", font=("Barlow", 18 , "Bold"), bg="yellow")
message.place(x=150, y=600)

create_button = Button(root, text="Create", command=create)
create_button.place(x=10, y=150)

read_button = Button(root, text="Read", command=read)
read_button.place(x=80, y=150)

update_button = Button(root, text="Update", command=update)
update_button.place(x=150, y=150)

delete_button = Button(root, text="Delete", command=delete)
delete_button.place(x=230, y=150)

root.mainloop()



