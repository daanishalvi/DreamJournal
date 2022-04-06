from tkinter import *  
from tkinter import ttk 
from PIL import ImageTk, Image


#method will have to be further expanded in order to link it to other .py files  (maybe?)
def create_new():
    win = Toplevel(root)


root = Tk()
#root.geometry('1000x600')  #TEMP FIX FOR LOGO GLITCH
#root.geometry('500x1000') #THE LOGO IS GLITCHING OUT 
#root.geometry('1000x1000') #LOGO LOOKS FINE BUT EMPTY SPACE AT THE BOTTOM

root.title("DreamSeeker")
main = ttk.Frame(root)
main.grid()

img = ImageTk.PhotoImage(Image.open("logo.png"))
label = Label(main, image = img)
label.grid(row=0,columnspan=2)
label.config(height=500, width=450)


#these buttons create new windows. will have to be linked to the other windows during implementation 
btn_journal = Button(main, text="My Journal", command = create_new)
btn_add = Button(main, text="Add Dream", command = create_new)

btn_journal.grid(row=1, column=0)
btn_add.grid(row=1, column=1)

btn_add.config(height=4, width=31)
btn_journal.config(height=4, width=31)

#btn.config(height=5, width=20)
#btn1.config(height=5, width=20)

#btn.pack(pady = 10, side = LEFT)
#btn1.pack(pady = 10, side = RIGHT)





root.mainloop()
