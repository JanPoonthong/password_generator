import random
import string
from tkinter import Tk, Label, Button, StringVar, IntVar, Entry
from tkinter import Checkbutton, messagebox
from turtle import up

import pyperclip

# Set screen
root = Tk()
root.geometry("400x400")
root.title("Password Generator")

# Value
password_string = StringVar()
password_length = IntVar()
lowercase_status = IntVar()
uppercase_status = IntVar()
numbers_status = IntVar()
special_char_status = IntVar()

# Default password length
password_length.set(16)


def list_handler():
    pass1 = []
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_char = (' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')')

    char_types_list = (lowercase, uppercase, numbers, special_char)
    checkboxes = (lowercase_status.get(),
                  uppercase_status.get(),
                  numbers_status.get(),
                  special_char_status.get())

    for index, characters in enumerate(char_types_list):
        if checkboxes[index] == 1:
            for item in characters:
                pass1.append(item)
    return pass1


def generate():
    pass1 = list_handler()
    if pass1 == []:
        return messagebox.showerror("Error",
                                    "Choose at least one type of charachters")
    password = ""
    for i in range(password_length.get()):
        password += random.choice(pass1)
    password_string.set(password)


def copy_to_clipboard():
    random_password = password_string.get()
    pyperclip.copy(random_password)

# Draw
Label(root, text="PASSWORD GENERATOR", width="300", height="2",
      font=("Times", 20)).pack()

Label(root, text="Enter Password Length", width="100", height="1",
      font=("Helvetica", 16)).pack()
Entry(root, textvariable=password_length, width="30").pack()
Button(root, text="Generate Password", command=generate).pack()

Entry(root, textvariable=password_string, width="30").pack()
Button(root, text="Copy to clipboard", command=copy_to_clipboard).pack()

Checkbutton(root, text='a-z', variable=lowercase_status).pack()
Checkbutton(root, text='A-Z', variable=uppercase_status).pack()
Checkbutton(root, text='0-9', variable=numbers_status).pack()
Checkbutton(root, text='!@#$%^&*()', variable=special_char_status).pack()
lowercase_status.set(1)

if __name__ == "__main__":
    root.mainloop()
