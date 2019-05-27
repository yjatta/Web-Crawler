from tkinter import *

root = Tk()
root.title("Web Crawler")
root.geometry('640x640+0+0')

name = Label(root, text='Project Name')
homepage = Label(root, text='Home Page')
name.grid(row=0, sticky=W)

homepage.grid(row=1, sticky=W)


def printName(event):
    print("Yoromang jatta")


name_entry = Entry(root)
homepage_entry = Entry(root)

name_entry.grid(row=0, column=1)
homepage_entry.grid(row=1, column=1)
check = Checkbutton(root, text='Keep me sign in')
check.grid(columnspan=2)
crawl_button = Button(root, text='Crawl', fg='white', bg='green')
# crawl = Button(root, text='Crawl', fg='white', bg='green', command=printName)
crawl_button.bind("<Button-1>",printName)
crawl_button.grid(columnspan=2)
root.mainloop()
