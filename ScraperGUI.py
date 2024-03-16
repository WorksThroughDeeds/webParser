from sre_constants import JUMP
from tkinter import *
from bs4 import BeautifulSoup
import requests





class EX:
    def __init__(self, root):
        root.title("Hello World!")
        root.geometry("1280x500")
        root.maxsize(1300,600)

        label = Label(root, text="Some text")
        label.pack()
        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        entry.pack()

        button = Button(root, text="Click Me", command=self.press_button)
        button.pack()
    
    def press_button(self):
        url = self.entry_text.get()
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")
        parsed_data = ' '

        for p in soup.find_all('p'):
            parsed_data += p.get_text() + ' '

        topl = Toplevel()
        label = Label(topl, text=parsed_data, width=150)
        label.pack()
        scrolly = Scrollbar(topl, orient=VERTICAL, width=18)
        scrolly.pack(side=RIGHT, fill=Y)
            
        
        
        

        
    

root = Tk()
EX(root)
root.mainloop()