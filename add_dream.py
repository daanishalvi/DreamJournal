#add dream
from tkinter import *
from tkinter import ttk
add_dream_window = Tk()
add_dream_window.title("Add Dream")
add_dream_window.geometry('400x400')
title = Label(add_dream_window, text = "Dream Title").pack()
title_entry = Entry(add_dream_window).pack()
colour_code = Label(add_dream_window,text = "Colour Code").pack()
colour_code_entry = Entry(add_dream_window).pack()
description = Label(add_dream_window,text = "Description").pack()
activate = Button(add_dream_window, text = "Activate Text-To-Speech").pack()
description_textbox = Text(add_dream_window, height = 100, width = 100).pack()

add_dream_window.mainloop()

