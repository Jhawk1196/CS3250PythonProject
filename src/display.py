import tkinter as tk
from tkinter import *
from tkinter import font
import webbrowser
from src import fontSelect
from src.parser import parse_url_feed
from src.gui_config import Configuration


def display(args):  # pragma: no cover
    root = Tk()
    root.title("Harry Parser and the Sorcerer's Feed's")
    go = BooleanVar()
    go.set(True)

    config = Configuration(args)
    size = IntVar()
    size.set(config.font_size)
    color = StringVar()
    color.set(config.font_color)
    family = StringVar()
    family.set(config.font_family)
    background = StringVar()
    background.set(config.background_color)
    time_var = IntVar()
    time_var.set(config.time)
    # Updated upstream
    menubar = Menu(root)

    cycle_menu = Menu(menubar)
    cycle_menu.add_command(label="5 seconds", command=lambda: [time_var.set(5000), root.update()])
    cycle_menu.add_command(label="10 seconds", command=lambda: [time_var.set(10000), root.update()])
    cycle_menu.add_command(label="15 seconds", command=lambda: [time_var.set(15000), root.update()])
    cycle_menu.add_command(label="30 seconds", command=lambda: [time_var.set(30000), root.update()])
    cycle_menu.add_command(label="60 seconds", command=lambda: [time_var.set(60000), root.update()])
    menubar.add_cascade(label="Cycle Time", menu=cycle_menu)

    font_menu = Menu(menubar)
    font_menu.add_command(label="Times New Roman",
                          command=lambda: [fontSelect.font_style(custom_font, 'Times'),
                                           family.set('Times'), root.update()])
    font_menu.add_command(label="Arial", command=lambda: [fontSelect.font_style(custom_font, 'Arial'),
                                                          family.set('Arial'), root.update()])
    font_menu.add_command(label="Helvetica",
                          command=lambda: [fontSelect.font_style(custom_font, 'Helvetica'),
                                           family.set('Helvetica'), root.update()])
    font_menu.add_command(label="Verdana",
                          command=lambda: [fontSelect.font_style(custom_font, 'Verdana'),
                                           family.set('Verdana'), root.update()])
    font_menu.add_command(label="Wingdings",
                          command=lambda: [fontSelect.font_style(custom_font, 'Wingdings'),
                                           family.set('Wingdings'), root.update()])
    menubar.add_cascade(label="Font", menu=font_menu)

    size_menu = Menu(menubar)
    size_menu.add_command(label="10 pt", command=lambda: [fontSelect.font_size(custom_font, 10),
                                                          size.set(10), root.update()])
    size_menu.add_command(label="11 pt", command=lambda: [fontSelect.font_size(custom_font, 11),
                                                          size.set(11), root.update()])
    size_menu.add_command(label="12 pt", command=lambda: [fontSelect.font_size(custom_font, 12),
                                                          size.set(12), root.update()])
    size_menu.add_command(label="13 pt", command=lambda: [fontSelect.font_size(custom_font, 13),
                                                          size.set(13), root.update()])
    size_menu.add_command(label="14 pt", command=lambda: [fontSelect.font_size(custom_font, 14),
                                                          size.set(14), root.update()])
    size_menu.add_command(label="15 pt", command=lambda: [fontSelect.font_size(custom_font, 15),
                                                          size.set(15), root.update()])
    size_menu.add_command(label="16 pt", command=lambda: [fontSelect.font_size(custom_font, 16),
                                                          size.set(16), root.update()])
    menubar.add_cascade(label="Font Size", menu=size_menu)

    font_color = Menu(menubar)
    font_color.add_command(label="Black", command=lambda: [fontSelect.font_color(label, 'black'),
                                                           color.set('black'), root.update()])
    font_color.add_command(label="White", command=lambda: [fontSelect.font_color(label, 'white'),
                                                           color.set('white'), root.update()])
    font_color.add_command(label="Red", command=lambda: [fontSelect.font_color(label, 'red'),
                                                         color.set('red'), root.update()])
    font_color.add_command(label="Blue", command=lambda: [fontSelect.font_color(label, 'blue'),
                                                          color.set('blue'), root.update()])
    font_color.add_command(label="Green", command=lambda: [fontSelect.font_color(label, 'green'),
                                                           color.set('green'), root.update()])
    menubar.add_cascade(label="Font Color", menu=font_color)

    gui_color = Menu(menubar)
    gui_color.add_command(label="Black",
                          command=lambda: [label.configure(background='black'), root.configure(background='black'),
                                           background.set('black'), root.update()])
    gui_color.add_command(label="White",
                          command=lambda: [label.configure(background='white'), root.configure(background='white'),
                                           background.set('white'), root.update()])
    gui_color.add_command(label="Red",
                          command=lambda: [label.configure(background='red'), root.configure(background='red'),
                                           background.set('red'), root.update()])
    gui_color.add_command(label="Blue",
                          command=lambda: [label.configure(background='blue'), root.configure(background='blue'),
                                           background.set('blue'), root.update()])
    gui_color.add_command(label="Green",
                          command=lambda: [label.configure(background='green'), root.configure(background='green'),
                                           background.set('green'), root.update()])
    menubar.add_cascade(label="GUI Background Color", menu=gui_color)

    exit_menu = Menu(menubar)
    exit_menu.add_command(label="Save and exit",
                          command=lambda: [go.set(False),
                                           save_values(config, time_var.get(), size.get(), color.get(),
                                                       background.get(), family.get()),
                                           time_var.set(0), root.quit()])
    exit_menu.add_command(label="Exit without Saving", command=lambda: [go.set(False), time_var.set(0), root.quit()])
    menubar.add_cascade(label="Exit Program", menu=exit_menu)

    root.configure(background=config.background_color)
    root.config(menu=menubar)
    custom_font = font.Font(family=config.font_family, size=config.font_size)
    label = Message(root, font=custom_font, fg=config.font_color, cursor="pirate", )
    label.config(width=750, background=config.background_color, padx=10, pady=10, anchor='center')

    root.minsize(750, 50)
    root.maxsize(750, 200)
    iteration = 0
    while go.get() is True:
        if iteration == 0:
            iteration = 1
            feed = update_feed(args, config.urls)
            node1 = feed.head
            temp_list = node1.data
            node2 = temp_list.head
            temp_dict = node2.data
        elif node2.next is None:
            if node1.next is None:
                feed = update_feed(args, config.urls)
                node1 = feed.head
            else:
                node1 = node1.next
            temp_list = node1.data
            node2 = temp_list.head
            temp_dict = node2.data
        else:
            node2 = node2.next
            temp_dict = node2.data
        var_title = StringVar()
        var_title.set(temp_dict["RSS_String"])
        label.config(textvariable=var_title)
        label.pack(fill=tk.BOTH, expand=True)
        label.bind("<Button-1>", lambda e: callback(temp_dict["Link"]))
        root.update_idletasks()
        root.update()
        root.after(time_var.get(), label.pack_forget())


def callback(url: str):  # pragma: no cover
    webbrowser.open_new(url)


def update_feed(args, config):  # pragma: no cover
    if config is None:
        raise Exception("There is no Configuration Yaml File")

    if args.url is not None:
        feed = parse_url_feed(args.url)
    elif args.file is not None:
        feed = parse_url_feed(args.file)
    else:
        feed = parse_url_feed(config)
    return feed


def save_values(config, time, size, color, background, family): # pragma: no cover
    save_dict = {'time': time, 'font_size': size, 'font_color': color,
                 'background_color': background, 'font_family': family}
    config.save_configuration(save_dict)
