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
 
 
class VisualPinboard():
    def __init__(self,description):
        self.description = description

def get_description_info(self):
    text = self.description
    nouns = [word for word, pos in pos_tag(word_tokenize(text)) if pos.startswith('NN')]
    # print(nouns)

    for noun in nouns:
        # print(noun)
        getImages(self,noun)

def getImages(self,word):
    a1 = "https://pixabay.com/api/?key=16344627-110e29474f27c28a4a9923a6a&q="
    words = word #the nouns entered in the dream description
    a2 = '+'.join(words.split(' '))
    #print(a2)
    a3 = "&safesearch=true&order=popular"
    res = requests.get(a1+a2+a3)
    #print(res)
    data = res.json()
    # print(data)
    val = storeImages(data['hits'][0:1],word)
    # print(len(data['hits'])) #gives back 20 pics, trying it to make it give back 1

    # self.description.delete(0, END)

def saveImage(image,dir):
    with open(dir+ '/' + "image1"+".jpg", "wb") as f:
        r1 = requests.get(image["largeImageURL"])
        f.write(r1.content)    

def storeImages(imagelist, name):
    folder_num = 1
    dir = "folder{}".format(folder_num)
    

    while os.path.exists(dir):
        folder_num +=1
        dir = "folder{}".format(folder_num)
    else:
        folder_num +=1
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
        

# vb = VisualPinboard("I was running away from wolves chasing me when I found a red feather on the floor and then I woke up")
# get_description_info(vb)


 
# if __name__ == '__main__':
 
#     root = Tk()
#     root.title("Scraping images from pixabay")
#     root.geometry("500x1000")
#     root.resizable(False, False)
 
 
 
    # dream_description = Label(root, text = "Enter the dream description")
    
    # getwords = Entry(root, width = 35)
    # btn = Button(root, text = "Generate Visual Pinboard", command = get_description_info)
 
 
 
    # dream_description.pack(pady = 20)
    # getwords.pack(pady = 20)
    # btn.pack(pady = 20)
    # getwords.focus()
 
 
 
    # root.mainloop()


#the folders need to be deleted after being uploaded to dream breakdown page 


# dream_description = "I was running away from wolves chasing me when I found a red feather on the floor and then I woke up"