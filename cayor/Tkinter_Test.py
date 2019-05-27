import tkinter

root = tkinter.Tk()
the_label = tkinter.Label(root, text='Web Crawler')
the_label.pack(fill=tkinter.X)
top_frame = tkinter.Frame(root)
top_frame.pack()
bottom_frame = tkinter.Frame(root)
bottom_frame.pack(side=tkinter.BOTTOM)

button1 = tkinter.Button(top_frame, text='Button 1', fg='red')
button2 = tkinter.Button(top_frame, text='Button 2', fg='blue')
button3 = tkinter.Button(top_frame, text='Button 3', fg='green')
button4 = tkinter.Button(bottom_frame, text='Button 4', fg='purple')

button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.LEFT)
button3.pack(side=tkinter.LEFT)
button4.pack(fill=tkinter.X)

root.mainloop()
