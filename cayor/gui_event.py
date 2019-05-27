from tkinter import *

root = Tk()

def leftclick(event):
    print('Left')

def middleclick(event):
    print('Middle')

def rightClick(event):
    print('Right')

frame = Frame(root, width=300, height=250)
frame.bind('<Button-1>', leftclick)
frame.bind('<Button-2>', middleclick)
frame.bind('<Button-3>', rightClick)

frame.pack()

root.mainloop()
