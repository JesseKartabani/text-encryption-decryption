# A simple tkinter window
import tkinter as tk
from tkinter import ttk
from tkinter import font

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --


root = tk.Tk()
# set window size
root.geometry("375x398")
# set window title
root.title("Title Here")

# static label
label = ttk.Label(root, padding=10, text="Enter text for encryption and decryption")
label.config(font=("calbri",13), foreground="black")
label.pack()

label1 = ttk.Label(root, text="Enter secret key for encryption and decryption")
label1.config(font=("calibri",13))
label1.place(x=10, y=170)

# widget allows user to input text
user_entry = tk.Entry (root)
user_entry.config()
user_entry.pack(pady=10)

root.mainloop()