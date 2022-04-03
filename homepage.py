from tkinter import *   
from PIL import ImageTk, Image


#method will have to be further expanded in order to link it to other .py files  (maybe?)
def create_new():
    win = Toplevel(root)


root = Tk()
root.geometry('1000x600')  #TEMP FIX FOR LOGO GLITCH
#root.geometry('500x1000') #THE LOGO IS GLITCHING OUT 
#root.geometry('1000x1000') #LOGO LOOKS FINE BUT EMPTY SPACE AT THE BOTTOM

root.title("DreamSeeker")

#these buttons create new windows. will have to be linked to the other windows during implementation 
btn = Button(root, text="My Journal", command = create_new)
btn1 = Button(root, text="Add Dream", command = create_new)

btn.config(height=5, width=20)
btn1.config(height=5, width=20)

btn.pack(pady = 10, side = LEFT)
btn1.pack(pady = 10, side = RIGHT)


img = ImageTk.PhotoImage(Image.open("logo.png"))


label = Label(root, image = img)
label.pack()

root.mainloop()