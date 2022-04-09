import speech_recognition as sr
import tkinter as tk

obj = tk.Tk()
obj.title("SpeechToText")
obj.geometry('400x200')
obj.resizable(0,0)

def rec():
    r = sr.Recognizer()
    #msg.configure(text="Say something")
    while True:
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            txt = r.recognize_google(audio)
            msg.configure(text=txt)
            print(txt)
        except Exception as e:
            print(e)
            break

msg = tk.Label()
msg.grid(row=0,column=0)
btn = tk.Button(text="Start",command=rec)
btn.grid(row=2,column=0)
obj.mainloop()