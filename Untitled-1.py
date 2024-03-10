from tkinter import *



class labelTest:

    def __init__(self, root):
        root.title("buttontest")
        button = Button(root, text="Click!", command=self.press_button)
        button.pack()

    def press_button(self):
        tlevel = Toplevel()
        label = Label(tlevel, text="Hello! :)")
        label.pack()




root = Tk()
labelTest(root)
root.mainloop()