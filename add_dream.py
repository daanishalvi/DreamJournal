#add dream
from string import whitespace
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor, width
from PIL import ImageGrab, ImageDraw
import PIL
import io
import datetime
from csv import *
add_dream_window = Tk()
add_dream_window.title("Add Dream")
#add_dream_window.geometry('400x500')

main = ttk.Frame(add_dream_window)
main.grid()

title = ttk.Label(main, text = "Dream Title")
title_entry = ttk.Entry(main, textvariable=tk.StringVar())

colour_code = ttk.Label(main, text = "Colour Code")
colour_code_entry = ttk.Entry(main, textvariable=tk.StringVar())
title.grid(row=0, columnspan=2, padx=200)
title_entry.grid(row=1, columnspan=2)
colour_code.grid(row=2, columnspan=2)
colour_code_entry.grid(row=3, columnspan=2)

description = ttk.Label(main,text = "Description")
activate = ttk.Button(main, text = "Activate Text-To-Speech")
description_textbox = Text(main, height = 10, width = 48)
description.grid(row=4, columnspan=2)
activate.grid(row=5, columnspan=2)
description_textbox.grid(row=6, columnspan=2)

csv_out_lst = []

def save_text():
        if title_entry.get() == '' or colour_code_entry.get() == '' or description_textbox.get(1.0, "end-1c") == '':
                messagebox.showerror("error", "Please fill the fields provided!")
                
        else:
                dream_date = datetime.datetime.now()
           
                lst = [title_entry.get(), colour_code_entry.get(), description_textbox.get(1.0, "end-1c"), dream_date.strftime("%x")]
                csv_out_lst.append(lst)
                
                with open("dream_data.csv", "a", encoding='UTF8', newline='') as f:
                        writing = writer(f)
                        writing.writerow([" ", " ", " "])
                        writing.writerows(csv_out_lst)
                messagebox.showinfo("Information", "Successfully saved your dream!")


save_button = ttk.Button(main, text="Save Dream", command = save_text)
save_button.grid(row=7, columnspan=2)

lastx, lasty = 0, 0

color = "#000000"
thickness = 1
small = 1
medium = 3
large = 5
xlarge = 10

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color, width=thickness)
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y

def changecolor(new):
    global color
    color = new

def changethickness(new):
    global thickness
    thickness = new

    
cfrm = ttk.Frame(main, borderwidth=2, relief='ridge')
cfrm.grid(row=8, columnspan=2)


red = "#ff0000"
blue = "#0000ff"
green = "#00ff00"
yellow = "#fafd0f"
black = "#000000"
white = "#ffffff"
button_r = ttk.Button(cfrm, text="RED", command=lambda: changecolor(red))
button_g = ttk.Button(cfrm, text="GREEN", command=lambda: changecolor(green))
button_b = ttk.Button(cfrm, text="BLUE", command=lambda: changecolor(blue))
button_y = ttk.Button(cfrm, text="YELLOW", command=lambda: changecolor(yellow))
button_bl = ttk.Button(cfrm, text="BLACK", command=lambda: changecolor(black))
button_w = ttk.Button(cfrm, text="ERASER", command=lambda: changecolor(white))
button_s = ttk.Button(cfrm, text="SMALL", command=lambda: changethickness(small))
button_m = ttk.Button(cfrm, text="MEDIUM", command=lambda: changethickness(medium))
button_l = ttk.Button(cfrm, text="LARGE", command=lambda: changethickness(large))
button_xl = ttk.Button(cfrm, text="XLARGE", command=lambda: changethickness(xlarge))
canvas = tk.Canvas(cfrm, bg=white)
button_r.grid(column=0, row=0)
button_g.grid(column=1, row=0)
button_b.grid(column=2, row=0)
button_y.grid(column=3, row=0)
button_bl.grid(column=4, row=0)
button_w.grid(column=0, row=1)
button_s.grid(column=1, row=1)
button_m.grid(column=2, row=1)
button_l.grid(column=3, row=1)
button_xl.grid(column=4, row=1)
canvas.grid(column=0, row=2, columnspan=5)
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

image = PIL.Image.new("RGB", (100,100), white)
draw = ImageDraw.Draw(image)

def save():
    x=main.winfo_rootx()+cfrm.winfo_x()
    y=main.winfo_rooty()+cfrm.winfo_y()
    print('canvas.x:', canvas.winfo_x())
    print('canvas.y:', canvas.winfo_y())
    print('canvas.rootx:', canvas.winfo_rootx())
    print('canvas.rooty:', canvas.winfo_rooty())
    print('main.rootx:', main.winfo_rootx())
    print('main.rooty:', main.winfo_rooty())
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    im = ImageGrab.grab((x, y, x1, y1))
    im.save("captured.png")
##def save():
##    main.update()
##    canvas.update()
##    x=canvas.canvasx()
##    y=canvas.canvasy()
##    x1=x+canvas.winfo_width()
##    y1=y+canvas.winfo_height()
##    im = ImageGrab.grab((x, y, x1, y1))
##    im.save("captured.png")

    #image.save("captured.png")
##    cnv = getscreen().getcanvas() 
##    global hen
##    ps = cnv.postscript(colormode = 'color')
##    hen = filedialog.asksaveasfilename(defaultextension = '.jpg')
##    im = Image.open(io.BytesIO(ps.encode('utf-8')))
##    im.save(hen + '.jpg')
def callback():
    print('  root.geometry:', main.winfo_geometry())
    print('canvas.geometry:', canvas.winfo_geometry())
    print('canvas.width :', canvas.winfo_width())
    print('canvas.height:', canvas.winfo_height())
    print('canvas.x:', canvas.winfo_x())
    print('canvas.y:', canvas.winfo_y())
    print('canvas.rootx:', canvas.winfo_rootx())
    print('canvas.rooty:', canvas.winfo_rooty())

btn_save = ttk.Button(main,text="SAVE",command=save)
btn_save.grid(row=9, columnspan=2)

add_dream_window.mainloop()



"""from tkinter import *
from tkinter import ttk
add_dream_window = Tk()
add_dream_window.title("Add Dream")
add_dream_window.geometry('400x600')
title = Label(add_dream_window, text = "Dream Title").pack()
title_entry = Entry(add_dream_window).pack()
colour_code = Label(add_dream_window,text = "Colour Code").pack()
colour_code_entry = Entry(add_dream_window).pack()
description = Label(add_dream_window,text = "Description").pack()
activate = Button(add_dream_window, text = "Activate Text-To-Speech").pack()
description_textbox = Text(add_dream_window, height = 100, width = 100).pack()

add_dream_window.mainloop()"""

