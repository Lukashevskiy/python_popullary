import tkinter
from PIL import Image, ImageTk

# import tkinter

window = tkinter.Tk()

window.title("Hello World")
window.geometry("640x480")


#checkbutton
checkbox = tkinter.Checkbutton(window, text="CHeck  your orientation").pack()

#button
button = tkinter.Button(window, text="not alive").pack()

#label
label = tkinter.Label(window, text="Not dead").pack()


#canvas
image = Image.open("tatras.jpg")
image_for_tk = ImageTk.PhotoImage(image)

canvas = tkinter.Canvas(window, height=400, width=700)
img = canvas.create_image(0, 0, anchor='nw',image=image_for_tk)

canvas.pack()

window.mainloop()