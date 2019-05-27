from tkinter import *


class GUITkinter:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text='Click me', command=self.printIt)
        self.printButton.pack(side=LEFT)
        self.quit = Button(frame, text='Quit', command=frame.quit)
        self.quit.pack(side=LEFT)

    def printIt(self):
        print("Waw this awesome")


root = Tk()
b = GUITkinter(root)
root.mainloop()






