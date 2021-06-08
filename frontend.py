import json
import download
from tkinter import *
import backend
import sqlite3

with open("config.json", "r") as f:
    credentials=json.load(f)
    username_o=credentials["username"]
    password_o=credentials["password"]

def bytte():
    backend.switch(username_o, password_o)
    e4.delete(0, END)
    e4.insert(END, "Byttet")

def down():
    download.download_d()
    e3.delete(0, END)
    e3.insert(END, "Lastet ned")

def delete():
    backend.delete()


window=Tk()
window.wm_title("Altibox switcher")

l1=Label(window, text="Email/username:")
l1.grid(row=0, column=0)

l2=Label(window, text="Password:")
l2.grid(row=1, column=0)

username_t=StringVar()
e1=Entry(window, textvariable=username_t)
e1.grid(row=0, column=1)

passw=StringVar()
e2=Entry(window, textvariable=passw)
e2.grid(row=1, column=1)

success=StringVar()
success="Ikke lastet ned"
e3=Entry(window, textvariable=success)
e3.grid(row=3, column=1)
e3.insert(END, success)

success1=StringVar()
success1="Ikke byttet"
e4=Entry(window,textvariable=success1)
e4.grid(row=4, column=1)
e4.insert(END, success1)


b1=Button(window, text="Download Chromium", width=17, command=down)
b1.grid(row=3, column=0)

b2=Button(window, text="Bytt", width=17, command=bytte) 
b2.grid(row=4, column=0)

b3=Button(window, text="Lagre brukernavn og password", width=35) # add command
b3.grid(row=2, column=0, columnspan=2)

b4=Button(window, text="Slett chromium", width=35, command=delete)
b4.grid(row=5, column=0, columnspan=2)









window.mainloop()


