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
root.geometry("375x398")
# set window title
root.title("Title Here")

label = ttk.Label(root, padding=10, text="Tkinter Window")
label.config(font=("Robote",20))
label.pack()

root.mainloop()