from tkinter import Tk, Label, Button
# import tkinter

window = Tk()

window.title("Hello World")
window.geometry("640x480")

def add_label():
    Label(window, text="Hello World").pack()

button = Button(window, text="Пам пам", command=add_label)

button.pack()
window.mainloop()