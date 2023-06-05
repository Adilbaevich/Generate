import tkinter
from tkinter import ttk
import string
import random

window = tkinter.Tk()
window.geometry('480x250')
window.resizable(False, False)

output_pass = tkinter.StringVar()

all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

def randPassGen():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)
        password = password + random.choice(char_type)

    output_pass.set(password)


pass_head = tkinter.Label(window, text='Password Length', width=40, font='Roboto 15').pack(pady=10)

pass_len = tkinter.IntVar()
length = tkinter.Spinbox(window, from_=7, to_=32, textvariable=pass_len, font='Roboto 15').pack()

btn = ttk.Button(window, command=randPassGen, text="Generate Password").pack(pady=10)

pass_label = tkinter.Label(window, text='Random Generated Password', width=25, font='Roboto 15').pack(pady="30 10")
tkinter.Entry(window, textvariable=output_pass, width=24, font='Roboto 15').pack()

window.mainloop()