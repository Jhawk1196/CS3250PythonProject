import yaml
from src.argument_parser import parse_args
import os

args = parse_args()


class Configuration:
    def make_defaults(
            self):
        """Defaults for GUI, fonts and test URL """
        self.font_color = "black"
        self.font_size = 12
        self.background_color = "white"
        self.urls = ["https://xkcd.com/atom.xml"]
        self.font_family = "Helvetica"
        self.time = 5000
        self.window_placement = None

    def load_yaml(
            self):
        """Accesses user given .yml file to load saved configuration """
        if args.config:
            config_file = args.config[0]
            # todo this should be in a try block to catch bad formatting
            with open(config_file) as f:
                self.conf_dict = yaml.load(f, Loader=yaml.FullLoader)
        else:
            entries = os.scandir('src/')
            use_this = ""
            for entry in entries:
                if entry.name == "saved_config.yml":
                    use_this = entry
                    break
                elif entry.name == "default_config.yml":
                    use_this = entry
                else:
                    continue

            with open(use_this) as f:
                self.conf_dict = yaml.load(f, Loader=yaml.FullLoader)

    def __init__(
            self, args):
        """
        If arguments are provided via command line, load_yaml is called to for saved configuration
        Sets default values for GUI using make_defaults method, then loads any saved configurations from .yml
        :param args: command line arguments
        """
        if args:
            self.load_yaml()

        self.make_defaults()

        if 'font_size' in self.conf_dict:
            self.font_size = self.conf_dict['font_size']
        if 'font_color' in self.conf_dict:
            self.font_color = self.conf_dict['font_color']
        if 'urls' in self.conf_dict:
            self.urls = self.conf_dict['urls']
        if 'background_color' in self.conf_dict:
            self.background_color = self.conf_dict['background_color']
        if 'font_family' in self.conf_dict:
            self.font_family = self.conf_dict['font_family']
        if 'time' in self.conf_dict:
            self.time = self.conf_dict['time']
        if 'window_placement' in self.conf_dict:
            self.window_placement = self.conf_dict['window_placement']

    def print_configuration(
            self):
        """Prints configuration to console """
        print('font size:' + str(self.font_size))
        print('font color:' + self.font_color)
        print('background color:' + self.background_color)
        print('urls:' + self.urls)

    def font_size(
            self):
        """
        returns font size of given font
        :return: font size
        """
        return self.font_size

    def font_color(
            self):
        """
        returns font color stored in given Message (label)
        :return: font color
        """
        return self.font_color

    def background_color(
            self):
        """
        returns background color stored in given Message (label)
        :return: background color
        """
        return self.background_color

    def urls(
            self):
        """
        returns web address for given URL
        :return: url
        """
        return self.urls

    def time(
            self):
        """
        returns constantly incremented time value at current point
        :return: time
        """
        return self.time

    def window_placement(
            self):
        """
        returns the window placement values
        :return: window_placement
        """
        return self.window_placement

    def save_configuration(
            self, save_info: dict):
        """
        Saves user selected (or default) settings for GUI and urls
        :param save_info: a dictionary containing saved preferences for GUI and urls
        """
        save_info['urls'] = self.urls
        with open('src/saved_config.yml', 'w') as file:
            yaml.dump(save_info, file)
