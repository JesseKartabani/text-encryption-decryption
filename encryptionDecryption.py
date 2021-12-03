import base64
import tkinter as tk
from tkinter import Button, Label, PhotoImage, Text, Toplevel, ttk, font, messagebox
from tkinter.constants import END, GROOVE, WORD

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

def decrypt():
    """ Decrypts user inputed text using base64 and displays it in a new window"""

    password = user_pass.get()
    # checks password is correct
    if password == "1234":
        root2 = Toplevel(root)        # creates new window
        root2.title("Decryption")     # sets window title
        root2.geometry("400x200")     # sets window size
        root2.configure(bg="#00bd56") # sets window background color

        message = user_text.get(1.0, "end") # stores user input

        # Decrypts message
        decode_message = message.encode("ascii") 
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        # displays DECRYTED in the top left
        Label(root2, text="DECRYPTED", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)

        # displays empty text box
        text1 = Text(root2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text1.place(x=10, y=40, width= 380, height=150)

        # displays the actual decrytped text
        text1.insert(END, decrypt)
    # displays error message when password field is empty
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    # displays error message when password is incorrect
    else:
        messagebox.showerror("Encryption", "Invalid Password")

def encrypt():
    """ Encrypts user inputed text using base64 and displays it in a new window """

    password = user_pass.get()
    # checks password is correct
    if password == "1234":
        root1 = Toplevel(root)        # creates new window
        root1.title("Encryption")     # sets window title
        root1.geometry("400x200")     # sets window size
        root1.configure(bg="#ed3833") # sets window background color

        message = user_text.get(1.0, "end") # stores user input

        # encodes message
        encode_message = message.encode("ascii") 
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        # displays ENCRYTED in the top left
        Label(root1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)

        # displays empty text box
        text1 = Text(root1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text1.place(x=10, y=40, width= 380, height=150)

        # displays the actual encrytped text
        text1.insert(END, encrypt)
    # displays error message when password field is empty
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    # displays error message when password is incorrect
    else:
        messagebox.showerror("Encryption", "Invalid Password")
        
    

def reset():
    """ Removes all user inputed text when reset button is clicked """

    user_text.delete("1.0", "end")
    user_pass.delete("0", "end")

# MAIN SCREEN

root = tk.Tk()
# set window size
root.geometry("400x400")
# set minimum window size value
root.minsize(400, 400)
# set maximum window size value
root.maxsize(400, 400)
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
Button(text="ENCRYPT", height=2, width=18, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=25, y=280)

# displays DECRYPT button
# 1. button calls decrypt function on click
Button(text="DECRYPT", height=2, width=18, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=280)

# displays RESET button
# 1. button calls reset function on click
Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=-15, y=330)

# displays a copy to clipboard button
# 1. button calls copy function on click

### TODO

root.mainloop()