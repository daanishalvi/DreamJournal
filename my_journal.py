from tkinter import *
from tkinter import ttk

class Journal():
    def __init__(self, title):
        self.title = title
 

    def create_journal(self):
        ''' Creates a page with different journal entries'''
        my_journal_window = Tk()
        my_journal_window.title("My Journal")
  
        main = ttk.Frame(my_journal_window)
        main.grid()