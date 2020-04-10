"""
This is very much a work in progress.
"""
import atexit
import yaml
from src.argument_parser import parse_args

args = parse_args()

def load_configuration(args):
    # check for yaml config file
    if args.config:
        config_file = args.config[0]
        # todo this should be in a try block to catch bad formatting
        with open(config_file) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

    else:
        config = []

def save_configuration(config):
    # can I just read the configuration elements from somewhere else?
    pass

def set_defaults():
    pass

# todone need config object
class Configuration(config):
    # todo no, the defaults should be here
    def __init__(self):
        self.conf_text = config

