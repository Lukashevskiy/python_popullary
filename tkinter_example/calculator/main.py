import tkinter
from PIL import Image, ImageTk
main_window = tkinter.Tk()

#set basic settings
main_window.title("base example with name 'Calculator'")

main_window.geometry("320x480")
# main_window.resizable(width=False, height=False)

main_window.columnconfigure(0, weight=1)
# main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)

main_window['bg'] = 'black'
#additional settings may be configured here using main_window['configure_key'] = 'value
# main_window['bg'] = 'black'
# main_window['font'] = ('Arial', 18)


#add frame to text on window
text_frame = tkinter.Frame(main_window)
text_frame['bg'] = 'black'

text_frame.columnconfigure(0, weight=1)
# text_frame.rowconfigure(0, weight=1)
# text_frame.rowconfigure(1, weight=4)

#add fame to mainframe
text_frame.grid(column=0, row=0, sticky=(tkinter.E, tkinter.W, tkinter.N, tkinter.S))

#expression
expression_frame = tkinter.Label(text_frame)

expression_frame['bg'] = 'black'
expression_frame['fg'] = 'grey'
expression_frame['font'] = ('Arial', 16)
expression_frame['text'] = "14+14+5="
expression_frame['padx'] = 15
expression_frame['pady'] = 5
expression_frame.grid(row=0, column=0, sticky=(tkinter.E))

#calculated value
value_frame = tkinter.Label(text_frame)

value_frame['bg'] = 'black'
value_frame['fg'] = 'White'
value_frame['font'] = ('Arial', 36)
value_frame['text'] = "122"
value_frame['padx'] = 15
value_frame.grid(row=1, column=0, sticky=(tkinter.E))



#add frame to buttons on window

def add_number(event):
    global expression_frame
    expr = int(event.widget['text'])
    if expr > 0:
        expression_frame['text'] += f'+{expr}'
    else:
        expression_frame['text'] += f'{expr}'
def clear_expr(event):
    global expression_frame
    expression_frame['text'] = ''

button_frame = tkinter.Frame(main_window)
button_frame['bg'] = 'black'
button_frame['padx'] = 10
button_frame['pady'] = 10
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

print(tkinter.Button().keys())
buttons = []
for i in range(0, 5):
    buttons_line = []
    for j in range(0, 4):
        button = tkinter.Button(button_frame, text='  ')

        # button['relief'] = 'flat'
        button['bg'] = 'black'
        button['fg'] = 'white'
        button['pady'] = 0
        button['padx'] = 0
        button['bd'] = 0
        button['font'] = 'Arial','18'
        button['activebackground'] = 'white'
        button['activeforeground'] = 'black'
        button['highlightcolor'] = 'white'
        button['highlightthickness'] = 0
        button.grid(row=i, column=j, sticky=(tkinter.E, tkinter.W, tkinter.N, tkinter.S))
    
        buttons_line.append(button)
    
    buttons.append(buttons_line)
buttons[0][0]['text'] = " C " 
buttons[0][0].bind("<Button-1>", clear_expr)
buttons[0][1]['text'] = "CE"
for i in range(1, 4):
    for j in range(0, 3):
        buttons[4-i][j]['text'] = f' {(i-1)*3+j + 1} '
        buttons[4-i][j].bind('<Button-1>', add_number)

buttons[-1][0]['text'] = "+/-"
buttons[-1][1]['text'] = ' 0 '
buttons[-1][2]['text'] = ' . '

buttons[0][-1]['text'] = ' / '
buttons[1][-1]['text'] = ' x '
buttons[2][-1]['text'] = ' - '
buttons[3][-1]['text'] = ' + '
buttons[4][-1]['text'] = ' = '

image = Image.open('./src/assets/backspace.png')
# image = image.resize((20, 40))

# buttons[0][2].image = tkinter.PhotoImage(image)
buttons[0][2]['text'] = " < "
button_frame.grid(column=0, row=1, sticky=(tkinter.E, tkinter.W, tkinter.N, tkinter.S))

# print(*main_window.__dir__(), sep='\n')



main_window.mainloop()
