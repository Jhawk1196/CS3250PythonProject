from tkinter import *


def helloWorld(feed):
    root = Tk()
    w = Label(root, text=str(feed))
    w.pack()
    root.mainloop()
