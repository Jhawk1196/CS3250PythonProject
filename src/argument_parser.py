import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Select a file or feed to "
                                                 "parse.")
    parser.add_argument('--url', dest='url', action='store', default=None,
                        help="enter a url of an RSS or ATOM feed to parse",
                        nargs='*')
    parser.add_argument('--file', dest='file', action='store', default=None,
                        help="enter a file name to parse", nargs='*')
    parser.add_argument('--config', dest='config', action='store', default='',
                        help="optionally enter a .yaml config file", nargs='*')
    args = parser.parse_args()
    return args


"""
This parses the command line arguments.
We can easily add more later with more parser.add_argument.
Examples: python main.py --url "http://rss.cnn.com/rss/cnn_us.rss"
          python main.py --file "some_file.json"
          python main.py --config "my_config.yaml"
          python main.py --help

The function will return an object with attributes .file and .url.
If one isn't specified it's an empty string.
"""

"""Tests are in their own file"""
