from tkinter import * 
from tkinter import filedialog
from tkinter import font
import tkinter as tk
from PIL import Image,ImageTk
import speech_recognition as sr
import pyttsx3
import wave
import os

gui = Tk(className=' SNOOP TEXT TO SPEECH CONVERTER')
gui.iconbitmap(r"images\snoop.ico")
gui.config(background='#e84e36')
# set window size
gui.geometry("1000x850")
gui.state('zoomed')

load = Image.open("images\Snoop-logos1.jpeg")

title_image = ImageTk.PhotoImage(load)
icon_button = Label(image = title_image, borderwidth= 0 )
icon_button.pack(pady=20)


def text_to_speech():
    gui.destroy()
    root = Tk(className=' SNOOP TEXT TO SPEECH CONVERTER')
    root.iconbitmap(r"images\snoop.ico")
    root.config(background='#e84e36')
    root.geometry("1000x850")
    root.state('zoomed')


    label2 = tk.Label(root, text="ENTER THE REQUIRED TEXT BELOW \n TO CONVERT INTO \n AUDIO FILE",
    font=('Arial Rounded MT Bold',30), bg = '#e84e36', fg= 'white')
    label2.pack()
    e= Entry(root, width= 450, font = ("Arial",40))
    e.pack(padx = 400, pady = 50)

    r = IntVar()
    r.set("1")


    Radiobutton(root, text = 'Female Voice', variable = r, value = 1, bg = '#e84e36', fg = 'white', selectcolor = '#e84e36', activebackground = 'cyan', font = ('Arial',20)).pack()
    Radiobutton(root, text = 'Male Voice', variable = r, value = 0,bg = '#e84e36', fg = 'white', selectcolor = '#e84e36', activebackground = 'cyan', font = ('Arial',20)).pack()
    
    x = StringVar()
    x.set(".mp3")
    Radiobutton(root, text = 'MP3 Format', variable = x, value = ".mp3", bg = '#e84e36', fg = 'white', selectcolor = '#e84e36', activebackground = 'cyan', font = ('Arial',10)).pack()
    Radiobutton(root, text = 'WAV Format', variable = x, value = ".wav",bg = '#e84e36', fg = 'white', selectcolor = '#e84e36', activebackground = 'cyan', font = ('Arial',10)).pack()
   


    def enter_text():
        a=e.get()
        print(a)
        input1 = a
        assistant = pyttsx3.init()
        voices = assistant.getProperty('voices')
        assistant.setProperty('voice', voices[r.get()].id)
        assistant.setProperty('rate', 170)
        assistant.runAndWait()
        assistant.say(input1)
        assistant.runAndWait()
    
    
    def save_audio():
        p = 'audio' + x.get()
        b=e.get()
        print(b)
        
        input2 = b
        assistant = pyttsx3.init()
        voices = assistant.getProperty('voices')
        assistant.setProperty('voice', voices[0].id)
        assistant.save_to_file(input2,p)
        assistant.runAndWait()

        
    

    play_button = PhotoImage(file = 'images\play.png')
    button3 = Button(root, image = play_button, background ='#e84e36',bd = 0, command= enter_text).pack(padx=50,pady=20,side=BOTTOM)

    save_button = PhotoImage(file = 'images\SAVE.png')
    button4 = Button(root, image = save_button, background ='#e84e36',bd = 0, command= save_audio).pack(padx=50,pady=20,side=BOTTOM)

    root.mainloop()

def speech_to_text():
    gui.destroy()
    root = Tk(className=' SNOOP TEXT TO SPEECH CONVERTER')
    root.iconbitmap(r"images\snoop.ico")
    root.config(background='#e84e36')
    root.geometry("1000x850")
    root.state('zoomed')
    label3 = tk.Label(root, text= 'THE BOT WILL IMMEDIATELY START RECORDING AFTER PRESSING START BUTTON', font=('Arial Rounded MT Bold',20), bg = '#e84e36', fg= 'white')
    label3.pack()
    
    text2 = ''
    def start():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            # r.energy_threshold()
            #print("(listening....)")
            
            audio= r.listen(source)
            text2 = r.recognize_google(audio)
        
        def convert():
            label5 = tk.Label(root, text= text2, font=('Arial Rounded MT Bold',20), bg = '#e84e36', fg= 'white')
            label5.pack()
        convert = Button(root, text = 'CONVERT', command = convert).pack()
    
    start = Button(root, text = "START RECORDING",font=('Arial Rounded MT Bold',60), command = start).pack()
    
    root.mainloop()

blogo = PhotoImage(file = "images\logo1.png")
blogo2 = PhotoImage(file = "images\logo2.png")


button1 = Button(gui, image = blogo,bd=0,background='#e84e36', command=text_to_speech).pack(side = RIGHT)
button2 = Button(gui, image = blogo2,bd=0,background='#e84e36', command = speech_to_text).pack(side = LEFT)


gui.mainloop()