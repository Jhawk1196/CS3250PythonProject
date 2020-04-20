"""
This is very much a work in progress
"""
import atexit
import yaml
from src.argument_parser import parse_args

args = parse_args()


def save_configuration(config):
    # can I just read the configuration elements from somewhere else?

    pass

def set_defaults():
    pass

# todone need config object
class Configuration:
    def __init__(self, args):
        # check for yaml config file
        if args.config:
            config_file = args.config[0]
            # todo this should be in a try block to catch bad formatting
            with open(config_file) as f:
                self.conf_dict = yaml.load(f, Loader=yaml.FullLoader)

        else:
            self.conf_dict = []
        self.font_size = self.conf_dict['font_size']
        self.font_color = self.conf_dict['font_color']
        self.urls = self.conf_dict['urls']
        self.background_color = self.conf_dict['background_color']

    def print_configuration(self):
        print('font size:' + str(self.font_size))
        print('font color:' + self.font_color)
        print('background color:' + self.background_color)
        print('urls:' + self.urls)


