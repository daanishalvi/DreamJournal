from tkinter import *
from tkinter import ttk
import csv

class Journal():
    def __init__(self, title):
        self.title = title
 

    def create_journal(self):
        ''' Creates a page with different journal entries'''
        my_journal_window = Tk()
        my_journal_window.geometry("500x500")
        my_journal_window.title("My Journal")
  
        main = ttk.Frame(my_journal_window)
        main.grid()

        # opening csv file with dream data to read
        file = open('dream_data.csv')
        csvreader = csv.reader(file)

        rows = []
        for row in csvreader:
                rows.append(row)

        print(rows)

        page_title = ttk.Label(main, text = "My Journal").grid(row=1, column=0)
        
        sort_by_label = ttk.Label(main, text = "Sort by").grid(row=2, column=0)

        for row in rows[1:]:
            dream_entry = ttk.Button(main, text="{}".format(row[0])).grid(row=3, column=0)

        my_journal_window.mainloop()

    
j = Journal('Journal1')
j.create_journal()