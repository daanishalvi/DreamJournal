try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from string import whitespace
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor, width
from PIL import ImageGrab, ImageDraw, Image, ImageTk
import PIL
import io
from csv import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, dream_breakdown, PageTwo, add_dream):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        
        main = ttk.Frame(self)
        main.grid()

        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        label = tk.Label(main, image = self.img)
        label.grid(row=0,columnspan=2)
        label.config(height=600, width=460)


        # These are linked properly 
        btn_journal = Button(main, text="My Journal", command=lambda: controller.show_frame("dream_breakdown"))
        btn_add = Button(main, text="Add Dream", command=lambda: controller.show_frame("add_dream"))

        btn_journal.grid(row=1, column=0)
        btn_add.grid(row=1, column=1)

        btn_add.config(height=4, width=32)
        btn_journal.config(height=4, width=32)


class dream_breakdown(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the dream_breakdown", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class add_dream(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.title("Add Dream")
        self.main = ttk.Frame(self)
        self.main.grid()
        
        # Title and Colour Code
        self.title = ttk.Label(self.main, text = "Dream Title")
        self.title_entry = ttk.Entry(self.main, textvariable=tk.StringVar())
        self.colour_code = ttk.Label(self.main, text = "Colour Code")
        self.colour_code_entry = ttk.Entry(self.main, textvariable=tk.StringVar())

        self.title.grid(row=0, columnspan=2, padx=200)
        self.title_entry.grid(row=1, columnspan=2)
        self.colour_code.grid(row=2, columnspan=2)
        self.colour_code_entry.grid(row=3, columnspan=2)

        # Description             
        self.description = ttk.Label(self.main,text = "Description")
        self.activate = ttk.Button(self.main, text = "Activate Text-To-Speech")
        self.description_textbox = Text(self.main, height = 10, width = 48)
        self.description.grid(row=4, columnspan=2)
        self.activate.grid(row=5, columnspan=2)
        self.description_textbox.grid(row=6, columnspan=2)

        self.csv_out_lst = []

        #self.save_button = ttk.Button(self.main, text="Save Dream", command = self.save_text)
        #self.save_button.grid(row=7, columnspan=2)

        self.lastx = 0
        self.lasty = 0
        self.color = "#000000"
        self.thickness = 1

        self.cfrm = ttk.Frame(self.main, borderwidth=2, relief='ridge')
        self.cfrm.grid(row=7, columnspan=2)


        # Canvas items (buttons and the actual canvas board)
        button_r = ttk.Button(self.cfrm, text="RED", command=lambda: self.changecolor("#ff0000"))
        button_g = ttk.Button(self.cfrm, text="GREEN", command=lambda: self.changecolor("#00ff00"))
        button_b = ttk.Button(self.cfrm, text="BLUE", command=lambda: self.changecolor("#0000ff"))
        button_y = ttk.Button(self.cfrm, text="YELLOW", command=lambda: self.changecolor("#fafd0f"))
        button_bl = ttk.Button(self.cfrm, text="BLACK", command=lambda: self.changecolor("#000000"))
        button_w = ttk.Button(self.cfrm, text="ERASER", command=lambda: self.changecolor("#ffffff"))
        button_s = ttk.Button(self.cfrm, text="SMALL", command=lambda: self.changethickness(1))
        button_m = ttk.Button(self.cfrm, text="MEDIUM", command=lambda: self.changethickness(3))
        button_l = ttk.Button(self.cfrm, text="LARGE", command=lambda: self.changethickness(5))
        button_xl = ttk.Button(self.cfrm, text="XLARGE", command=lambda: self.changethickness(10))
        self.canvas = tk.Canvas(self.cfrm, bg="#ffffff")
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
        self.canvas.grid(column=0, row=2, columnspan=5)
        self.canvas.bind("<Button-1>", self.xy)
        self.canvas.bind("<B1-Motion>", self.addLine)

        btn_save = ttk.Button(self.main,text="SAVE DREAM",command=self.save)
        btn_save.grid(row=8, columnspan=2)

        self.image = 0
        

    def save(self):

        if self.title_entry.get() == '' or self.colour_code_entry.get() == '' or self.description_textbox.get(1.0, "end-1c") == '':
                messagebox.showerror("error", "Please fill the fields provided!")
                
        else:
                lst = [self.title_entry.get(), self.colour_code_entry.get(), self.description_textbox.get(1.0, "end-1c")]
                self.csv_out_lst = [lst]
                
                with open("dream_data.csv", "a", encoding='UTF8', newline='') as f:
                        writing = writer(f)
                        writing.writerow([" ", " ", " "])
                        writing.writerows(self.csv_out_lst)

                self.title_entry.delete(0, 'end')
                self.colour_code_entry.delete(0, 'end')
                self.description_textbox.delete('1.0', 'end')

                # just grab the position of the canvas widget relative to the screen origin
                x = self.canvas.winfo_rootx()
                y = self.canvas.winfo_rooty()

                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                bbox = (x * 2, y * 2, x1 * 2, y1 * 2)
                # wuh?? internal pixel coordinate system is different than screen coordinates
                # https://github.com/python-pillow/Pillow/issues/3293
                # last comment
                # print(bbox)
                # sys.stdout.flush()
                im = ImageGrab.grab(bbox)
                im.save("image" + str(self.image) + ".png")

                self.canvas.delete('all')
                
                messagebox.showinfo("Information", "Successfully saved your dream!")
                self.controller.show_frame("StartPage")
        

    def xy(self, event):
        self.lastx, self.lasty = event.x, event.y
    def addLine(self, event):
        self.canvas.create_line((self.lastx, self.lasty, event.x, event.y), fill=self.color, width=self.thickness)
        # this makes the new starting point of the drawing
        self.lastx, self.lasty = event.x, event.y

    def changecolor(self, new):
        self.color = new

    def changethickness(self, new):
        self.thickness = new


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
