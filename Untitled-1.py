

import curses
import site
from textwrap import fill
from tkinter import *
from turtle import width
from urllib import request
from bs4 import BeautifulSoup
import requests



class labelTest:

    def __init__(self, root):
        root.title("buttontest")
        button = Button(root, text="Click!", command=self.press_button)
        button.pack()

    def press_button(self):
        sitePull = "https://en.wikipedia.org/wiki/YouTube"
        res = requests.get(sitePull)
        soup = BeautifulSoup(res.content, "html.parser")
        parsedStrings = " "
        for p in soup.find_all('p'):
            parsedStrings += soup.get_text()

    
        tlevel = Toplevel()
        canvas = Canvas(tlevel, width=30)
        canvas.pack()
        tlevel.geometry("1200x500")
        label = Label(canvas, text=parsedStrings)
        label.pack()
        scrolly = Scrollbar(tlevel, orient=VERTICAL, width=17)
        scrolly.pack(side=RIGHT, fill="y")
        
    

        



        #listbox = Listbox(tlevel, width=500, height=1200)
        #listbox.pack()
        #tlevel.geometry("1280x720")
        




root = Tk()
labelTest(root)
root.mainloop()