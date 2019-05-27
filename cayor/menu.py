from tkinter import *


def donothing():
    print('Something cool')


root = Tk(className='Crawler')
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Project ..' , command=donothing)
submenu.add_command(label='New', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=root.quit)

root.mainloop()