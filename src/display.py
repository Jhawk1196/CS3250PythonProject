from tkinter import *
import tkinter as tk


def helloWorld(feed):
    root = Tk()
    var = StringVar()
    label = Message(root, textvariable=var)  # relief=RAISED
    window_text = label.cget("text")
    var.set(feed)

    root.geometry("500x500")

    button = tk.Button(text="Click and Quit", command=root.quit)
    button.pack()

    label.pack()
    root.mainloop()
    return window_text

"""
while display is not quitting:
    while list is not finished:
        iterate through the list
    if the list does end:
        update the list
"""