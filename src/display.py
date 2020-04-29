import tkinter as tk  # pragma: no cover
import webbrowser  # pragma: no cover
from tkinter import *  # pragma: no cover
from tkinter import font  # pragma: no cover
from src import fontSelect  # pragma: no cover
from src.gui_config import Configuration  # pragma: no cover
from src.parser import parse_url_feed  # pragma: no cover

root: Tk = Tk()  # pragma: no cover


def update_feed(
        args, config):  # pragma: no cover
    """
    Checks command line arguments and .yml config file to create feed list
    :param args: arguments from command line
    :param config: .yml configuration file
    :return: Linked List of feeds ()
    """
    if config is None:
        raise Exception("There is no Configuration Yaml File")
    if args.url is not None:
        feed = parse_url_feed(args.url)
    elif args.file is not None:
        feed = parse_url_feed(args.file)
    else:
        feed = parse_url_feed(config)
    return feed


def callback(
        url: str):  # pragma: no cover
    """Opens selected URL in browser"""
    webbrowser.open_new(url)


class Display:  # pragma: no cover
    def __init__(
            self):  # pragma: no cover
        """Initiates GUI settings"""
        self.size = IntVar()
        self.time_var = IntVar()

        self.color = StringVar()
        self.family = StringVar()
        self.background = StringVar()
        self.var_title = StringVar()

        self.go = BooleanVar()
        self.iteration = BooleanVar()

        self.go.set(True)
        self.iteration.set(False)
        self.w = 800
        self.h = 50
        self.x = None
        self.y = None

        self.label = None
        self.config = None
        self.node1 = None
        self.node2 = None

    def display(
            self, args):  # pragma: no cover
        """
        Sets up GUI with drop down menus to change config settings
        :param args: command line arguments
        """
        root.title("Harry Parser and the Sorcerer's Feeds")

        self.config = Configuration(args)
        self.size.set(self.config.font_size)
        self.color.set(self.config.font_color)
        self.family.set(self.config.font_family)
        self.background.set(self.config.background_color)
        self.time_var.set(self.config.time)
        # Updated upstream
        menubar = Menu(root)

        # Menu to select how long each site appears in display
        cycle_menu = Menu(menubar)
        cycle_menu.add_command(label="5 seconds", command=lambda: [self.time_var.set(5000), root.update()])
        cycle_menu.add_command(label="10 seconds", command=lambda: [self.time_var.set(10000), root.update()])
        cycle_menu.add_command(label="15 seconds", command=lambda: [self.time_var.set(15000), root.update()])
        cycle_menu.add_command(label="30 seconds", command=lambda: [self.time_var.set(30000), root.update()])
        cycle_menu.add_command(label="60 seconds", command=lambda: [self.time_var.set(60000), root.update()])
        menubar.add_cascade(label="Cycle Time", menu=cycle_menu)

        # Menu to select font family
        font_menu = Menu(menubar)
        font_menu.add_command(label="Times New Roman", command=lambda: [
            fontSelect.font_style(custom_font, 'Times'), self.family.set('Times'), root.update()])
        font_menu.add_command(label="Arial", command=lambda: [
            fontSelect.font_style(custom_font, 'Arial'), self.family.set('Arial'), root.update()])
        font_menu.add_command(label="Helvetica", command=lambda: [
            fontSelect.font_style(custom_font, 'Helvetica'), self.family.set('Helvetica'), root.update()])
        font_menu.add_command(label="Verdana", command=lambda: [
            fontSelect.font_style(custom_font, 'Verdana'), self.family.set('Verdana'), root.update()])
        font_menu.add_command(label="Wingdings", command=lambda: [
            fontSelect.font_style(custom_font, 'Wingdings'), self.family.set('Wingdings'), root.update()])
        menubar.add_cascade(label="Font", menu=font_menu)

        # Menu to select font size
        size_menu = Menu(menubar)
        size_menu.add_command(label="10 pt", command=lambda: [
            fontSelect.font_size(custom_font, 10), self.size.set(10), root.update()])
        size_menu.add_command(label="11 pt", command=lambda: [
            fontSelect.font_size(custom_font, 11), self.size.set(11), root.update()])
        size_menu.add_command(label="12 pt", command=lambda: [
            fontSelect.font_size(custom_font, 12), self.size.set(12), root.update()])
        size_menu.add_command(label="13 pt", command=lambda: [
            fontSelect.font_size(custom_font, 13), self.size.set(13), root.update()])
        size_menu.add_command(label="14 pt", command=lambda: [
            fontSelect.font_size(custom_font, 14), self.size.set(14), root.update()])
        size_menu.add_command(label="15 pt", command=lambda: [
            fontSelect.font_size(custom_font, 15), self.size.set(15), root.update()])
        size_menu.add_command(label="16 pt", command=lambda: [
            fontSelect.font_size(custom_font, 16), self.size.set(16), root.update()])
        menubar.add_cascade(label="Font Size", menu=size_menu)

        # Menu to select font color
        font_color = Menu(menubar)
        font_color.add_command(label="Black", command=lambda: [
            fontSelect.font_color(self.label, 'black'), self.color.set('black'), root.update()])
        font_color.add_command(label="White", command=lambda: [
            fontSelect.font_color(self.label, 'white'), self.color.set('white'), root.update()])
        font_color.add_command(label="Red", command=lambda: [
            fontSelect.font_color(self.label, 'red'), self.color.set('red'), root.update()])
        font_color.add_command(label="Blue", command=lambda: [
            fontSelect.font_color(self.label, 'blue'), self.color.set('blue'), root.update()])
        font_color.add_command(label="Green", command=lambda: [
            fontSelect.font_color(self.label, 'green'), self.color.set('green'), root.update()])
        menubar.add_cascade(label="Font Color", menu=font_color)

        # Menu to select GUI background color
        gui_color = Menu(menubar)
        gui_color.add_command(label="Black", command=lambda: [
            self.label.configure(background='black'), root.configure(background='black'),
            self.background.set('black'), root.update()])
        gui_color.add_command(label="White", command=lambda: [
            self.label.configure(background='white'), root.configure(background='white'),
            self.background.set('white'), root.update()])
        gui_color.add_command(label="Red", command=lambda: [
            self.label.configure(background='red'), root.configure(background='red'),
            self.background.set('red'), root.update()])
        gui_color.add_command(label="Blue", command=lambda: [
            self.label.configure(background='blue'), root.configure(background='blue'),
            self.background.set('blue'), root.update()])
        gui_color.add_command(label="Green", command=lambda: [
            self.label.configure(background='green'), root.configure(background='green'),
            self.background.set('green'), root.update()])
        menubar.add_cascade(label="GUI Background Color", menu=gui_color)

        # Menu to quit program with option to save settings as .yml configuration file
        exit_menu = Menu(menubar)
        exit_menu.add_command(label="Save and exit", command=lambda: [
            self.go.set(False), self.save_values(), self.time_var.set(0), root.destroy(), root.quit()])
        exit_menu.add_command(label="Exit without Saving", command=lambda: [
            self.go.set(False), self.time_var.set(0), root.destroy(), root.quit()])
        menubar.add_cascade(label="Exit Program", menu=exit_menu)

        root.configure(background=self.config.background_color)
        root.config(menu=menubar)
        custom_font = font.Font(family=self.config.font_family, size=self.config.font_size)
        self.label = Label(root, font=custom_font, fg=self.config.font_color, cursor="pirate")
        self.label.config(background=self.config.background_color, padx=10, pady=10, anchor='center')
        self.label.pack(fill=tk.BOTH, expand=True)
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        self.x = (ws / 2) - (self.w / 2)
        self.y = (hs / 2) - (self.h / 2)
        if self.config.window_placement is not None:
            root.geometry(self.config.window_placement)
        else:
            root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.display_message(args)
        # https://www.youtube.com/watch?v=gm-7kdgNDMk
        while self.go.get():
            try:
                for time in range(0, self.time_var.get(), 10):
                    root.after(4, root.update())
                    root.after(4, root.update_idletasks())
            except TclError:
                exit()
            self.display_message(args)

    def save_values(
            self):  # pragma: no cover
        """Saves current configurations as a .yml file"""
        save_dict = {'time': self.time_var.get(), 'font_size': self.size.get(), 'font_color': self.color.get(),
                     'background_color': self.background.get(), 'font_family': self.family.get(),
                     "window_placement": root.geometry()}
        self.config.save_configuration(save_dict)

    def display_message(
            self, args):  # pragma: no cover
        """Governs what messages are displayed in GUI and sets the URL to each feed to open in browser"""
        if not self.iteration.get():
            self.iteration.set(True)
            feed = update_feed(args, self.config.urls)
            self.node1 = feed.head
            temp_list = self.node1.data
            self.node2 = temp_list.head
            temp_dict = self.node2.data
        elif self.node2.next is None:
            if self.node1.next is None:
                feed = update_feed(args, self.config.urls)
                self.node1 = feed.head
            else:
                self.node1 = self.node1.next
            temp_list = self.node1.data
            self.node2 = temp_list.head
            temp_dict = self.node2.data
        else:
            self.node2 = self.node2.next
            temp_dict = self.node2.data

        self.var_title.set(temp_dict["RSS_String"])
        self.label.bind("<Button-1>", lambda e: callback(temp_dict["Link"]))
        self.label.config(textvariable=self.var_title)
