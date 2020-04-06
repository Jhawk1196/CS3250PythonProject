from tkinter import *
import tkinter as tk
from src.parser import parse_url_feed


def helloWorld(args):
    if args.url is not None:
        feed = parse_url_feed(args.url)
    elif args.file is not None:
        feed = parse_url_feed(args.file)
    else:
        feed = parse_url_feed("http://rss.cnn.com/rss/cnn_allpolitics.rss")

    root = Tk()
    var = StringVar()
    label = Message(root, textvariable=var)  # relief=RAISED
    var.set(feed)
    window_text = var.get()
    
    root.geometry("1000x500")

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