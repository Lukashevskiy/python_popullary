import tkinter
from tkinter import Tk

window = Tk()

window.title("Calculator")
window.geometry("640x480")

button_frame = tkinter.Frame(window, width=100)
display_frame = tkinter.Frame(window, width=100)

input_field = tkinter.Entry(display_frame, font=('arial', 36, 'bold'))
input_field.pack()
buttons = []


def to_white(x, y):
    print(x, y)


for i in range(1, 11):
    button_line = []
    for j in range(1, 11):
        button_line.append(
            tkinter.Button(
                button_frame,
                padx=5,
                pady=5,
                width=2,
                height=1,
                background='purple',
                text=f"{(i - 1) * 10 + j}",
                command=lambda: to_white(i, j)))
        
    buttons.append(button_line)

for i in range(0, 10):
    for j in range(0, 10):
        buttons[i][j].grid(row=i + 1, column=j + 1)

display_frame.pack()
button_frame.pack()
window.mainloop()
