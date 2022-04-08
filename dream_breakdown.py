from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class Dream():
    def __init__(self, title, color_code, description, drawing_path):
        self.title = title
        self.color_code = color_code
        self.description = description
        self.drawing_path = drawing_path
    
    def create_dream_entry(self):
        ''' Creates a dream entry with the data entered by the user'''
        
        dream_breakdown_window = Tk()
        dream_breakdown_window.title("Dream Breakdown")
  
        main = ttk.Frame(dream_breakdown_window)
        main.grid()


        dream_title_label = ttk.Label(main, text = "Dream Title")
        dream_title = ttk.Label(main, text = self.title)

        color_code_label = ttk.Label(main,text = "Color Code")
        color_code = ttk.Label(main,text = self.color_code)

        dream_title_label.grid(row=0,column=1,  columnspan=2, padx=200)
        dream_title.grid(row=0, column=10, columnspan=2, padx=200)

        color_code_label.grid(row=2, column=1, columnspan=2)
        color_code.grid(row=2, column=10, columnspan=2)

        dream_description_label = ttk.Label(main, text = "Description")
        dream_description = ttk.Label(main, text = self.description)

        dream_description_label.grid(row=4, column=1, columnspan=2)
        dream_description.grid(row=4, column=10, columnspan=2)

        #creating visual pinboard
        visual_pinboard_label = ttk.Label(main, text = "Visual Pinboard")
        visual_pinboard_label.grid(row=5, column=1, columnspan=5)

        
        #corner case statements need to be created for cases of having no nouns in description or just one.

        img1 = Image.open('logo.png')
        img1_photo = ImageTk.PhotoImage(img1)

        img2 = Image.open('logo.png')
        img2_photo = ImageTk.PhotoImage(img2)

        img3 = Image.open('logo.png')
        img3_photo = ImageTk.PhotoImage(img3)

        img3 = Image.open('logo.png')
        img1_photo = ImageTk.PhotoImage(img3)

       

        # img1.grid(row=5, column=10, columnspan=1/4)
        # img2.grid(row=5, column=10, columnspan=1/4)
        # img3.grid(row=5, column=10, columnspan=1/4)
        # img4.grid(row=5, column=10, columnspan=1/4)

        #creating drawing
        #loading the drawing 
        drawing = Image.open('logo.png')
        drawing_photo = ImageTk.PhotoImage(drawing)
        dream_drawing_label = ttk.Label(main, text = "Dream Drawing")
        dream_drawing = Label(main, image = drawing_photo, width = 40, height=50)

        dream_drawing_label.grid(row=6, column=1, columnspan=2)

        dream_drawing.grid(row=10, column=1, columnspan=2)






        dream_breakdown_window.mainloop()


#the dream object fields need to be filled by info from csv's or user inputted data in the add dream page. The one I filled is a template for testing
dream = Dream("Nightmare where I was chased by wolves", "black", "I was running away from big black wolves chasing me when I found a red feather on the floor and then I woke up", "logo.png")
dream.create_dream_entry()
        
