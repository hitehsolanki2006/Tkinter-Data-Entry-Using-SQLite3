from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Data Entry")
root.geometry('800x700+300+200')
root.resizable(False, False)
root.configure(bg="#6666ff")

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('SQLITE_DB.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    address TEXT,
    hobby TEXT,
    email TEXT,
    area_of_interest TEXT
)
''')
conn.commit()

def submit():
    name = namevalue.get()
    contact = contactEntry.get()
    age = AgeValue.get()
    gender = gender_combobox.get()
    address = addressEntry.get(1.0, END).strip()
    hobby = hobby_combobox.get()
    email = emailValue.get()
    area_of_interest = area_combobox.get()

    cursor.execute('''
    INSERT INTO data (full_name, phone_number, age, gender, address, hobby, email, area_of_interest)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, contact, age, gender, address, hobby, email, area_of_interest))
    conn.commit()
    
    messagebox.showinfo('info', 'Detail added!')
    clear()

def clear():
    namevalue.set('')
    contactValue.set('')
    AgeValue.set('')
    addressEntry.delete(1.0, END)
    hobby_combobox.set('')
    emailValue.set('')
    area_combobox.set('')

icon_image = PhotoImage(file="hunter_1.png")
root.iconphoto(False, icon_image)

Label(root, text="Please fill out this Entry form", font="arial 20", bg="#6666ff", fg="#fff").place(x=250, y=20)

Label(root, text="Name", font=23, bg="#6666ff", fg="#fff").place(x=50, y=100)
Label(root, text="Contact No", font=23, bg="#6666ff", fg="#fff").place(x=50, y=150)
Label(root, text="Age", font=23, bg="#6666ff", fg="#fff").place(x=50, y=200)
Label(root, text="Gender", font=23, bg="#6666ff", fg="#fff").place(x=380, y=200)
Label(root, text="Address", font=23, bg="#6666ff", fg="#fff").place(x=50, y=250)
Label(root, text="Hobby", font=23, bg="#6666ff", fg="#fff").place(x=50, y=350)
Label(root, text="Email", font=23, bg="#6666ff", fg="#fff").place(x=50, y=400)
Label(root, text="Area of Interest", font=23, bg="#6666ff", fg="#fff").place(x=50, y=450)

namevalue = StringVar()
contactValue = StringVar()
AgeValue = StringVar()
emailValue = StringVar()

nameEntry = Entry(root, textvariable=namevalue, width=45, bd=2, font=20)
contactEntry = Entry(root, textvariable=contactValue, width=45, bd=2, font=20)
ageEntry = Entry(root, textvariable=AgeValue, width=15, font=20)
emailEntry = Entry(root, textvariable=emailValue, width=45, bd=2, font=20)

gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='readonly', width=14)
gender_combobox.place(x=470, y=200)
gender_combobox.set('Male')

addressEntry = Text(root, width=50, height=4, bd=4)

# Hobby
hobby_combobox = Combobox(root, values=['Coding', 'Hacking', 'Other IT-related'], font='arial 14', state='readonly', width=14)
hobby_combobox.place(x=200, y=350)
hobby_combobox.set('Coding')

# Area of Interest
area_combobox = Combobox(root, values=["Cyber", "Developing", "Testing", "Research"], font='arial 14', state='readonly', width=14)
area_combobox.place(x=200, y=450)
area_combobox.set('Cyber')

nameEntry.place(x=200, y=100)
contactEntry.place(x=200, y=150)
ageEntry.place(x=200, y=200)
addressEntry.place(x=200, y=250)
emailEntry.place(x=200, y=400)

Button(root, text="Submit", bg="#3333ff", fg="white", width=15, height=2, command=submit).place(x=120, y=600)
Button(root, text="Clear", bg="#3333ff", fg="white", width=15, height=2, command=clear).place(x=340, y=600)
Button(root, text="Exit", bg="#3333ff", fg="white", width=15, height=2, command=lambda: root.destroy()).place(x=560, y=600)

root.mainloop()
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Data Entry")
root.geometry('800x700+300+200')
root.resizable(False, False)
root.configure(bg="#6666ff")

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('data_base.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    address TEXT,
    hobby TEXT,
    email TEXT,
    area_of_interest TEXT
)
''')
conn.commit()

def submit():
    name = namevalue.get()
    contact = contactEntry.get()
    age = AgeValue.get()
    gender = gender_combobox.get()
    address = addressEntry.get(1.0, END).strip()
    hobby = hobby_combobox.get()
    email = emailValue.get()
    area_of_interest = area_combobox.get()

    cursor.execute('''
    INSERT INTO data (full_name, phone_number, age, gender, address, hobby, email, area_of_interest)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, contact, age, gender, address, hobby, email, area_of_interest))
    conn.commit()
    
    messagebox.showinfo('info', 'Detail added!')
    clear()

def clear():
    namevalue.set('')
    contactValue.set('')
    AgeValue.set('')
    addressEntry.delete(1.0, END)
    hobby_combobox.set('')
    emailValue.set('')
    area_combobox.set('')

icon_image = PhotoImage(file="hunter_1.png")
root.iconphoto(False, icon_image)

Label(root, text="Please fill out this Entry form", font="arial 20", bg="#6666ff", fg="#fff").place(x=250, y=20)

Label(root, text="Name", font=23, bg="#6666ff", fg="#fff").place(x=50, y=100)
Label(root, text="Contact No", font=23, bg="#6666ff", fg="#fff").place(x=50, y=150)
Label(root, text="Age", font=23, bg="#6666ff", fg="#fff").place(x=50, y=200)
Label(root, text="Gender", font=23, bg="#6666ff", fg="#fff").place(x=380, y=200)
Label(root, text="Address", font=23, bg="#6666ff", fg="#fff").place(x=50, y=250)
Label(root, text="Hobby", font=23, bg="#6666ff", fg="#fff").place(x=50, y=350)
Label(root, text="Email", font=23, bg="#6666ff", fg="#fff").place(x=50, y=400)
Label(root, text="Area of Interest", font=23, bg="#6666ff", fg="#fff").place(x=50, y=450)

namevalue = StringVar()
contactValue = StringVar()
AgeValue = StringVar()
emailValue = StringVar()

nameEntry = Entry(root, textvariable=namevalue, width=45, bd=2, font=20)
contactEntry = Entry(root, textvariable=contactValue, width=45, bd=2, font=20)
ageEntry = Entry(root, textvariable=AgeValue, width=15, font=20)
emailEntry = Entry(root, textvariable=emailValue, width=45, bd=2, font=20)

gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='readonly', width=14)
gender_combobox.place(x=470, y=200)
gender_combobox.set('Male')

addressEntry = Text(root, width=50, height=4, bd=4)

# Hobby
hobby_combobox = Combobox(root, values=['Coding', 'Hacking', 'Other IT-related'], font='arial 14', state='readonly', width=14)
hobby_combobox.place(x=200, y=350)
hobby_combobox.set('Coding')

# Area of Interest
area_combobox = Combobox(root, values=["Cyber", "Developing", "Testing", "Research"], font='arial 14', state='readonly', width=14)
area_combobox.place(x=200, y=450)
area_combobox.set('Cyber')

nameEntry.place(x=200, y=100)
contactEntry.place(x=200, y=150)
ageEntry.place(x=200, y=200)
addressEntry.place(x=200, y=250)
emailEntry.place(x=200, y=400)

Button(root, text="Submit", bg="#3333ff", fg="white", width=15, height=2, command=submit).place(x=120, y=600)
Button(root, text="Clear", bg="#3333ff", fg="white", width=15, height=2, command=clear).place(x=340, y=600)
Button(root, text="Exit", bg="#3333ff", fg="white", width=15, height=2, command=lambda: root.destroy()).place(x=560, y=600)

root.mainloop()
