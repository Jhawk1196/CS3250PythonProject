from tkinter import *


def helloWorld():
    root = Tk()
    w = Label(root, text="Hello, world!")
    windowText = w.cget("text")
    w.pack()
    root.mainloop()
    return windowText
