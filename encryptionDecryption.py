# A simple tkinter window
import tkinter as tk
from tkinter import Button, Text, ttk
from tkinter.constants import GROOVE, WORD

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

def decrypt():
    """"""
    return None

def encrypt():
    """"""
    return None

def reset():
    """ Removes all user inputed text """

    user_text.delete("1.0", "end")

    

root = tk.Tk()
# set window size
root.geometry("400x400")
# set window title
root.title("Ciphertext")

# static label that tells user to input text
label = ttk.Label(root, padding=10, text="Enter text for encryption and decryption")
label.config(font=("calbri",13), foreground="black",)
label.pack()

# static label that asks for users password
label1 = ttk.Label(root, text="Enter secret key for encryption and decryption")
label1.config(font=("calibri",12))
label1.place(x=10, y=200)

# widget allows user to input their password
user_pass = tk.Entry (root)
user_pass.config(font="Robote 20", background="white", relief=GROOVE, bd=0, show="*")
user_pass.place(x=28, y=225)

# widget allows user to input their text
user_text = tk.Text (root, wrap=WORD)
user_text.config(font="calibri 13", background="white", relief=GROOVE, bd=0)
user_text.place(x=24, y=50, width=355, height=100)

# displays ENCRYPT button
# 1. button calls encrypt function on click
Button(text="ENCRYPT", height=2, width=18, bg="#ed3833", fg="white", bd=0, command="").place(x=25, y=280)

# displays DECRYPT button
# 1. button calls decrypt function on click
Button(text="DECRYPT", height=2, width=18, bg="#00bd56", fg="white", bd=0, command="").place(x=200, y=280)

# displays RESET button
# 1. button calls reset function on click
Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=-15, y=330)


root.mainloop()