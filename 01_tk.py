# from curses import BUTTON1_DOUBLE_CLICKED
from tkinter import *


root = Tk()
root.title("Keyapp")
root.geometry("700x450")
root.iconbitmap('Webalys-Kameleon.pics-Hacker.ico')

lbl = Label(root, text="Encryption", bg="Green")
lbl.place(x=20, y=40)
lbl2 = Label(root, text="Decryption", bg="Blue")
lbl2.place(x=20, y=80)

ent = Entry(root, bg="Black", fg="White", bd=5, font=("Algerian", "10"))
ent.place(x=100, y=40)
ent2 = Entry(root, bg="Black", fg="White", bd=5, font=("Algerian", "10"))
ent2.place(x=100, y=80)

btn = Button(root, text="Submit", bg="Yellow")
btn.place(x=20, y=150)


root.mainloop()
