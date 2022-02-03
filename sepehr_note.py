import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import *
import pyttsx3

m=0

sound=pyttsx3.init()
sound.setProperty('rate',100)
sound.say("I love my mum")
sound.runAndWait()

window=tk.Tk()

window.title('maman')

title=tk.Label(text='❤I love my mam❤',bg='#ffcc66',fg='#ffffff',width=200,height=1,font=('courier',25) )
text=tk.Text(width=200,height=24,bg='#ffcc66',fg='#ffffff',font=35)
btn_save=tk.Button(text='save',width=190,height=1,bg='#ffcc66',font=3)
btn_jsound=tk.Button(text='jsound',width=190,height=1,bg='#ffcc66',font=3)
btn_open=tk.Button(text='open file',width=190,height=1,bg='#ffcc66',font=3)
btn_color=tk.Button(text='choose color',width=190,height=1,bg='#ffcc66',font=3)
btn_font=tk.Button(text='choose font color ',width=190,height=1,bg='#ffcc66',font=3)
title.pack()
text.pack()
btn_save.pack()
btn_open.pack()
btn_jsound.pack()
btn_color.pack()
btn_font.pack()

def file(file):
    filedialog.asksaveasfile(initialdir='/',title='save as',filetypes=(('Text Document','*.txt'),('all files','*.*')))

def open_file(w):
    filedialog.askopenfilename(initialdir="/",title="open file",filetypes=(("Text Document","*.txt"),('all files','*.*')))

def color(w):
    color= askcolor()
    text.configure(bg=color[1])
def fount_color(w):
    color= askcolor()
    text.configure(fg=color[1])

def sound(w):
    
     sound=pyttsx3.init()
     sound.setProperty('rate',100)
     sound.say(text.get(1.0,tk.END))
     sound.runAndWait()
def sound_(w):
    while True:
        sound=pyttsx3.init()
        sound.setProperty('rate',100)
        sound.say(text.get(1.0,tk.END))
        sound.runAndWait()

btn_save.bind('<ButtonPress-1>',file)
btn_jsound.bind('<ButtonPress-1>',sound)
btn_jsound.bind('<ButtonPress-3>',sound_)
btn_open.bind('<ButtonPress-1>',open_file)
btn_color.bind('<ButtonPress-1>',color)
btn_font.bind('<ButtonPress-1>',fount_color)

window.mainloop()
