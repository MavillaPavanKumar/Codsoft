from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry("1000x500")
root.configure(bg="#7092BE")  

passwrd = StringVar()
passlen = IntVar()
passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)

def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
output_label = Label(root, textvariable=passwrd, width=40, font=("Arial", 15, "bold"), fg="white", bg="black")
output_label.pack(pady=10)

Label(root, text="Password Generator", font=("Agency FB", 40, "bold"), fg="white" , bg="#7092BE").pack()
Label(root, text="Enter the number to get password", font=("Segoe UI Variable Small Semibol", 20, "bold"), fg="black" , bg="#7092BE").pack(pady=3)
Entry(root, textvariable=passlen, width=30, font=("Arial", 10, "bold")).pack(pady=10)
Button(root, text="Tap to get", font=("Times New Roman", 15, "bold"), fg="black" , bg="white" , command=generate).pack(pady=3)
Button(root, text="Tap to copy clipboard", font=("Times New Roman", 15, "bold"), fg="black" , bg="white" , command=copyclipboard).pack()

root.mainloop()
