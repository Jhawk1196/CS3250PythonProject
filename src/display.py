from tkinter import *
import tkinter as tk


def helloWorld(feed):
    root = Tk()
    var = StringVar()
    label = Message(root, textvariable=var)  # relief=RAISED
    window_text = label.cget("text")
    var.set(feed)

    root.title("T2: RSS Feed Parser") # What will we call this program?
    root.geometry("500x500")

    button = tk.Button(text="Click and Quit", command=root.quit)
    button.pack()

    label.pack()
    root.mainloop()
    return window_text
