from tkinter import Tk, Label, Button, StringVar
import random

window = Tk()

window.title("Hello World")
window.geometry("640x480")


def add_label():
    global text
    number = random.randint(0, 100)
    text.set(number)

text = StringVar()
label = Label(window, textvariable=text)

button = Button(window, 
                text="Пам пам", 
                command=add_label)

label.pack()
button.pack()
window.mainloop()