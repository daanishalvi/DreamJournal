from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from visual_pinboard import VisualPinboard, get_description_info


class Dream():
    def __init__(self, title, color_code, description, path, date):
        self.title = title
        self.color_code = color_code
        self.description = description
        self.path = path
        self.date = date

    
    def create_dream_entry(self):
        ''' Creates a dream entry with the data entered by the user'''
        
        dream_breakdown_window = Tk()
        dream_breakdown_window.title("Dream Breakdown")
        
        #tried to use ttk.Style to change the background of the window, but was not successful 
        
        """s = ttk.Style()
        s.configure('f1', background = 'white')
        main = ttk.Frame(dream_breakdown_window, style = 'f1')"""
        
        
        
        main = ttk.Frame(dream_breakdown_window)
        main.grid()


        dream_title_label = ttk.Label(main, text = "Dream Title").grid(row=1,column=1,  columnspan=2, padx=200, pady=6)
        dream_title = ttk.Label(main, text = self.title).grid(row=1, column=10, columnspan=2, padx=200, pady=6)

        # # #forgot to add the date
        dream_date_label = ttk.Label(main, text = "Date").grid(row=2,column=1,  columnspan=2, padx=200, pady=6)
        dream_date = ttk.Label(main, text = self.date).grid(row=2, column=10, columnspan=2, padx=200, pady=6)

        color_code_label = ttk.Label(main,text = "Color Code").grid(row=3, column=1, columnspan=2, pady=6)
        color_code = ttk.Label(main,text = self.color_code).grid(row=3, column=10, columnspan=2, pady=6)

        dream_description_label = ttk.Label(main, text = "Description",).grid(row=4, column=1, columnspan=2, pady=6)
        dream_description = ttk.Label(main, text = self.description).grid(row=4, column=10, columnspan=2, pady=6)


        #creating visual pinboard
        visual_pinboard_label = ttk.Label(main, text = "Visual Pinboard").grid(row=6, column=1, columnspan=2, pady=6)
        vb = VisualPinboard("{}".format(self.description))
        get_description_info(vb)
        


        
        #corner case statements need to be created for cases of having no nouns in description or just one.

        img1 = Image.open('folder1/image1.jpg')
        img1_photo = ImageTk.PhotoImage(img1)
        img1_display = Label(main, image = img1_photo, width = 400, height=420).grid(row=8, column=1, columnspan=2)

        img2 = Image.open('folder2/image1.jpg')
        img2_photo = ImageTk.PhotoImage(img2)
        img2_display = Label(main, image = img2_photo, width = 400, height=420).grid(row=8, column=10, columnspan=2)

        img3 = Image.open('folder3/image1.jpg')
        img3_photo = ImageTk.PhotoImage(img3)
        img3_display = Label(main, image = img3_photo, width = 400, height=420).grid(row=8, column=17, columnspan=2)


    
        #creating drawing
        # loading the drawing 
        drawing = Image.open("{}".format(self.path))
        drawing_photo = ImageTk.PhotoImage(drawing)
        dream_drawing_label = ttk.Label(main, text = "Dream Drawing").grid(row=30, column=1, columnspan=2)
        dream_drawing = Label(main, image = drawing_photo, width = 40, height=50).grid(row=10, column=1, columnspan=2)


        dream_breakdown_window.mainloop()


#the dream object fields need to be filled by info from csv's or user inputted data in the add dream page. The one I filled is a template for testing
# dream = Dream("Nightmare where I was chased by wolves", "black", "I was running away from big black wolves chasing me when I found a red feather on the floor and then I woke up", "logo.png", "10/02/2022")
# dream.create_dream_entry()
        
