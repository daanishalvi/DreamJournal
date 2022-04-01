#Import the library tkinter
from tkinter import *

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, pos_tag
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen
import base64



# Create a GUI app
root = Tk()
root.geometry('1000x500')
root.title("Visual pinboard")
  

# The dream description from the dream object will go here the one I have right now is a template dream description
dream_description = "I was running away from big black wolves chasing me when I found a red feather on the floor and then I woke up"

def get_description_info(text):
  nouns = [word for word, pos in pos_tag(word_tokenize(text)) if pos.startswith('NN')]
  verbs = [word for word, pos in pos_tag(word_tokenize(text)) if pos.startswith('VB')]
  adjectives = [word for word, pos in pos_tag(word_tokenize(text)) if pos.startswith('JJ')]
  print(nouns)
  print(verbs)
  print(adjectives)
  return [nouns, verbs, adjectives]

get_description_info(dream_description)


api_info = {"key":"19607744-3a4a8d7b2c94a2cabcd68915d", "q": "wolf"}
r = requests.get("https://pixabay.com/api", params = api_info)
response = r.json()

type(response)
for hit in response['hits']:
  # print(hit)
  # print(hit['webformatURL'])
  image_url = hit['webformatURL']
  image_byt = urlopen(image_url).read()
  image_b64 = base64.encodestring(image_byt)
  photo = root.PhotoImage(data=image_b64)
  
  label = root.Label(image=photo)
  label.image = photo
  label.pack()


# Make the loop for displaying app
root.mainloop()