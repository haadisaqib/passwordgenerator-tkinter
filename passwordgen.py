import tkinter
import random
import string
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

symbols = [  "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=",  "[", "\"", "]", "'", ";", ":", "\"", "<", ",", ".", ">", "?", "/"]

app = tkinter.Tk()
app.title("Password Generator")
app.geometry("400x250")
icon = resource_path("passwordgenicon.ico")
app.iconbitmap(icon)
app.pack_propagate(0)

text_box = tkinter.Text(app, height=1, width=10)
text_box.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label = tkinter.Label(master=app,
                      text="Password Length:",
                      width=15,
                      height=25)
label.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)



def button_function():
    global password_result_field, password_result, textboxsize
    password_length = text_box.get("1.0", "end").strip()
    if not password_length.isdigit() or int(password_length) > 30:
        print("Please enter a valid number less than or equal to 30")
    else:
        password_length = int(password_length)
        password_result = ""
        for x in range(password_length):
            random_num = random.randint(1, 3)
            if random_num == 1:
                appendletter()
            elif random_num == 2:
                appendsym()
            else:
                appendnum()
        password_result_field.configure(state="normal")
        password_result_field.delete("1.0", "end")
        password_result_field.insert("1.0", password_result)
        password_result_field.configure(state="disabled")
        password_length = len(password_result)
        if password_length >= 30:
            password_result = "Max character limit is 30"
            textboxsize=10
        elif password_length >= 24:
            textboxsize=30
        elif password_length >= 18:
            textboxsize=25
        elif password_length >= 12:
            textboxsize=20
        elif password_length >= 6:
            textboxsize=15
        else:
            textboxsize=15
        password_result_field.configure(width=textboxsize)  # set the width of the widget


def appendletter():
    global password_result
    letters = string.ascii_letters
    random_letter = random.choice(letters)
    password_result += random_letter


def appendnum():
    global password_result
    digits = string.digits
    random_digit = random.choice(digits)
    password_result += random_digit


def appendsym():
    global password_result
    global symbols
    random_sym = random.choice(symbols)
    password_result += random_sym

password_result = ""
textboxsize = 0

password_result_field = tkinter.Text(master=app,
                                     width= textboxsize,
                                     height=1)
password_result_field.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


button = tkinter.Button(master=app, text="Generate Password", command=button_function)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

app.mainloop()
