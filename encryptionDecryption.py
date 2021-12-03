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
root.geometry("640x200")
root.title("Title Here")

label = ttk.Label(root, padding=10, text="Tkinter Window")
label.config(font=("Comic Sans MS",40))
label.pack()

root.mainloop()