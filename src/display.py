from tkinter import *
import tkinter as tk
from src.parser import parse_url_feed
from src import fontSelect
from tkinter import font


def display(args):
    # Stashed changes
    if args.url is not None:
        feed = parse_url_feed(args.url)
    elif args.file is not None:
        feed = parse_url_feed(args.file)
    # elif config file is not empty
        # feed = parse_url_feed(config file url_list)
    else:
        feed = parse_url_feed("http://rss.cnn.com/rss/cnn_allpolitics.rss")
    feed = str(feed)
    feed = feed.split()
    feed = [item.replace(",", "\n\n•") for item in feed]
    root = Tk()
    root.title("Team Woo")

    # Updated upstream
    menubar = Menu(root)
    var = StringVar()
    customfont = font.Font(family='Helvetica', size=12)
    label = Message(root, textvariable=var, font=customfont, fg='black', cursor="pirate")  # relief=RAISED
    label.configure(background='black', fg='white', cursor="pirate")
    var.set(feed)

    window_text = var.get()

    root.geometry("1000x500")

    fontmenu = Menu(menubar)
    fontmenu.add_command(label="Times New Roman",
                         command=lambda: [fontSelect.fontStyle(customfont, 'Times'), root.update()])
    fontmenu.add_command(label="Arial", command=lambda: [fontSelect.fontStyle(customfont, 'Arial'), root.update()])
    fontmenu.add_command(label="Helvetica",
                         command=lambda: [fontSelect.fontStyle(customfont, 'Helvetica'), root.update()])
    fontmenu.add_command(label="Verdana", command=lambda: [fontSelect.fontStyle(customfont, 'Verdana'), root.update()])
    fontmenu.add_command(label="Wingdings",
                         command=lambda: [fontSelect.fontStyle(customfont, 'Wingdings'), root.update()])
    menubar.add_cascade(label="Font", menu=fontmenu)

    sizemenu = Menu(menubar)
    sizemenu.add_command(label="10 pt", command=lambda: [fontSelect.fontSize(customfont, 10), root.update()])
    sizemenu.add_command(label="11 pt", command=lambda: [fontSelect.fontSize(customfont, 11), root.update()])
    sizemenu.add_command(label="12 pt", command=lambda: [fontSelect.fontSize(customfont, 12), root.update()])
    sizemenu.add_command(label="13 pt", command=lambda: [fontSelect.fontSize(customfont, 13), root.update()])
    sizemenu.add_command(label="14 pt", command=lambda: [fontSelect.fontSize(customfont, 14), root.update()])
    sizemenu.add_command(label="15 pt", command=lambda: [fontSelect.fontSize(customfont, 15), root.update()])
    sizemenu.add_command(label="16 pt", command=lambda: [fontSelect.fontSize(customfont, 16), root.update()])
    menubar.add_cascade(label="Font Size", menu=sizemenu)

    fontcolor = Menu(menubar)
    fontcolor.add_command(label="Black", command=lambda: [fontSelect.fontColor(label, 'black'), root.update()])
    fontcolor.add_command(label="White", command=lambda: [fontSelect.fontColor(label, 'white'), root.update()])
    fontcolor.add_command(label="Red", command=lambda: [fontSelect.fontColor(label, 'red'), root.update()])
    fontcolor.add_command(label="Blue", command=lambda: [fontSelect.fontColor(label, 'blue'), root.update()])
    fontcolor.add_command(label="Green", command=lambda: [fontSelect.fontColor(label, 'green'), root.update()])
    menubar.add_cascade(label="Font Color", menu=fontcolor)

    gui_color = Menu(menubar)
    gui_color.add_command(label="Black", command=lambda: [label.configure(background='black'), root.update()])
    gui_color.add_command(label="White", command=lambda: [label.configure(background='white'), root.update()])
    gui_color.add_command(label="Red", command=lambda: [label.configure(background='red'), root.update()])
    gui_color.add_command(label="Blue", command=lambda: [label.configure(background='blue'), root.update()])
    gui_color.add_command(label="Green", command=lambda: [label.configure(background='green'), root.update()])
    menubar.add_cascade(label="GUI Background Color", menu=gui_color)

    root.configure(background='#a5acaf')
    button = tk.Button(text="Click and Quit", command=root.quit, background='#69be28', fg='white', cursor="heart")
    button.pack()

    root.config(menu=menubar)
    label.pack()
    root.mainloop()

    return window_text
