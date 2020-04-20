"""
This is very much a work in progress
"""
import atexit
import yaml
from src.argument_parser import parse_args

args = parse_args()


# todone need config object
class Configuration:
    def make_defaults(self):
        # defaults:
        self.font_color = "black"
        self.font_size = 15
        self.background_color = "white"
        self.urls = "https://xkcd.com/atom.xml"

    def load_yaml(self):
        # check for yaml config file
        if args.config:
            config_file = args.config[0]
            # todo this should be in a try block to catch bad formatting
            with open(config_file) as f:
                self.conf_dict = yaml.load(f, Loader=yaml.FullLoader)
        else:
            self.conf_dict = []

    def __init__(self, args):
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

    def print_configuration(self):
        print('font size:' + str(self.font_size))
        print('font color:' + self.font_color)
        print('background color:' + self.background_color)
        print('urls:' + self.urls)

    def font_size(self):
        return self.font_size()

    def font_color(self):
        return self.font_color()

    def background_color(self):
        return self.background_color()

    def urls(self):
        return self.urls()

    def save_configuration(config):
        # can I just read the configuration elements from somewhere else?
        pass

# cf = Configuration(args)
#
# cf.print_configuration()