from tkinter import *


def helloWorld(feed):
    root = Tk()
    w = Label(root, text=str(feed))
    window_text = w.cget("text")
    w.pack()
    root.mainloop()
    return window_text
