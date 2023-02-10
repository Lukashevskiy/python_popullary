from tkinter import Tk, Label, Button, StringVar
import random

window = Tk()

window.title("Hello World")
window.geometry("640x480")

l, m, r = StringVar(), StringVar(), StringVar()
l.set(0)
r.set(100)      
m.set(50)
l_label = Label(window, textvariable=l)
r_label = Label(window, textvariable=r)
m_label = Label(window, textvariable=m)

l_label.grid(row=0, column=0)
r_label.grid(row=0, column=2)
m_label.grid(row=0, column=1)

def mm():
    global l, r, m
    m.set((int(l.get())+int(r.get()))//2)

def lt():
    global l, r, m
    r.set(m.get())
    mm()

def gr():
    global l, r, m
    l.set(m.get())
    mm()

button_lt = Button(window, text='Меньше', command=lt)
button_gr = Button(window, text='Больше', command=gr)
button_lt.grid(row=1, column=0)
button_gr.grid(row=1, column=2)

# l_label.pack()
# r_label.pack()

window.mainloop()