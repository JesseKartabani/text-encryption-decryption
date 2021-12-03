# A simple tkinter window
import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --


root = tk.Tk()
# set window size
root.geometry("400x400")
# set window title
root.title("Title Here")

# static label
label = ttk.Label(root, padding=10, text="Enter text for encryption and decryption")
label.config(font=("calbri",13), foreground="black")
label.pack()

# widget allows user to input text
user_entry = tk.Entry (root)
user_entry.config()
user_entry.pack(pady=10)

root.mainloop()