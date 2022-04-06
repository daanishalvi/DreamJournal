import os
import requests
import socket
import random
from tkinter import *
from tkinter.messagebox import *


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, pos_tag
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
 
 
try:
    socket.create_connection(("www.google.com",80))
    #showinfo("Connected","u r connected")
 
 
    def saveImage(image,dir):
        with open(dir+ '/' + str(image['id'])+".jpg", "wb") as f:
            r1 = requests.get(image["largeImageURL"])
            f.write(r1.content)    
 
    def storeImages(imagelist, name):
        mode = 0o666
        dir = "" + str(name)
        while os.path.exists(dir):
#please use your own default directory name like data:/ or e:/
            dir = "data:/" + str(name) + str(random.randrange(0,1000))
        else:
            os.mkdir(dir)
        #print(imagelist)
        for i in imagelist:
            val = i['largeImageURL'].rfind('.')
            extension = i['largeImageURL'][val+1:]
            if extension.lower() == 'jpg' or extension.lower() == 'png':
                saveImage(i,dir)
            else:
                pass
        return dir
            
    def getImages(word):
        a1 = "https://pixabay.com/api/?key=16344627-110e29474f27c28a4a9923a6a&q="
        words = word #the nouns entered in the dream description
        a2 = '+'.join(words.split(' '))
        #print(a2)
        a3 = "&safesearch=true&order=popular"
        res = requests.get(a1+a2+a3)
        #print(res)
        data = res.json()
        # print(data)
        val = storeImages(data['hits'][0:2],word)
        # print(len(data['hits'])) #gives back 20 pics, trying it to make it give back 1
  

        showinfo("Success",val + " directory created")
        getwords.delete(0, END)


    def get_description_info():
        text = getwords.get()
        nouns = [word for word, pos in pos_tag(word_tokenize(text)) if pos.startswith('NN')]
        # print(nouns)

        for noun in nouns:
            # print(noun)
            getImages(noun)

   
     
   
except Exception as e:
    showerror("issue", e)
 
if __name__ == '__main__':
 
    root = Tk()
    root.title("Scraping images from pixabay")
    root.geometry("500x1000")
    root.configure(background='#FF9196')
    root.resizable(False, False)
 
 
 
    dream_description = Label(root, text = "Enter the dream description", font = ('Arial', 18, 'bold'), bg = '#FF9196')
    
    getwords = Entry(root, width = 35,bd = 5, font = ('Arial', 18, 'bold'))
    btn = Button(root, text = "Generate Visual Pinboard", font = ('Arial', 18, 'bold'), command = get_description_info)
 
 
 
    dream_description.pack(pady = 20)
    getwords.pack(pady = 20)
    btn.pack(pady = 20)
    getwords.focus()
 
 
 
    root.mainloop()




