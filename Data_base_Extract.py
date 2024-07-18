from tkinter import *
from tkinter.ttk import Treeview
import sqlite3
from PIL import Image, ImageTk

# Create the main application window
root = Tk()
root.title("Database Information")
root.geometry('900x500+300+200')
root.configure(bg="#6666ff")

# Connect to SQLite database
conn = sqlite3.connect('SQLITE_DB.db')
cursor = conn.cursor()

# Background image
bg_image = Image.open("hunter_1.png")
bg_image = bg_image.resize((900, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Header image
header_image = Image.open("hunter_1.png")
header_image = header_image.resize((900, 100), Image.Resampling.LANCZOS)
header_photo = ImageTk.PhotoImage(header_image)

header_label = Label(root, image=header_photo)
header_label.place(x=0, y=0, relwidth=1)

# Treeview to display data
tree = Treeview(root, columns=('ID', 'Name', 'Phone', 'Age', 'Gender', 'Address', 'Hobby', 'Email', 'Interest'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Age', text='Age')
tree.heading('Gender', text='Gender')
tree.heading('Address', text='Address')
tree.heading('Hobby', text='Hobby')
tree.heading('Email', text='Email')
tree.heading('Interest', text='Interest')

tree.column('ID', width=30)
tree.column('Name', width=100)
tree.column('Phone', width=100)
tree.column('Age', width=30)
tree.column('Gender', width=50)
tree.column('Address', width=200)
tree.column('Hobby', width=100)
tree.column('Email', width=150)
tree.column('Interest', width=100)

# Fetch data from database
cursor.execute("SELECT * FROM data")
rows = cursor.fetchall()
for row in rows:
    tree.insert('', END, values=row)

tree.pack(expand=True, fill=BOTH)

# Run the application
root.mainloop()
