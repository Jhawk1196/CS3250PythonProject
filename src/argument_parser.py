import argparse
import unittest
from sys import argv


def parse_args():
    parser = argparse.ArgumentParser(description="Select a file or feed to parse.")
    parser.add_argument('--url', dest='url', action='store', default="",
                        help="enter a url of an RSS or ATOM feed to parse", nargs='*')
    parser.add_argument('--file', dest='file', action='store', default="",
                        help="enter a file name to parse", nargs='*')
    parser.add_argument('--config', dest='config', action='store', default='',
                        help ="optionally enter a .yaml config file", nargs='*')
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

"""Here be the tests"""


class ArgTests(unittest.TestCase):
    def test_single_url(self):
        argv[1:] = ["--url", "google.com"]
        args = parse_args()
        self.assertEqual(args.url, ['google.com'])
        self.assertEqual(args.file, "")
        self.assertEqual(args.config, "")

    def test_single_file(self):
        argv[1:] = ["--file", "some_file.json"]
        args = parse_args()
        self.assertEqual(args.file, ['some_file.json'])
        self.assertEqual(args.url, "")
        self.assertEqual(args.config, "")

    def test_single_config(self):
        argv[1:] = ["--config", "some_config.yaml"]
        args = parse_args()
        self.assertEqual(args.config, ['some_config.yaml'])
        self.assertEqual(args.url, "")
        self.assertEqual(args.file, "")

    def test_multiple_url(self):
        argv[1:] = ["--url", "google.com", "duckduckgo.com"]
        args = parse_args()
        self.assertEqual(args.url, ['google.com', "duckduckgo.com"])
        self.assertEqual(args.file, "")
        self.assertEqual(args.config, "")

    def test_urls_and_files(self):
        argv[1:] = ["--url", "google.com", "duckduckgo.com", "--file", "some_file.json", "another_file.json"]
        args = parse_args()
        self.assertEqual(args.url, ['google.com', "duckduckgo.com"])
        self.assertEqual(args.file, ["some_file.json", "another_file.json"])
        self.assertEqual(args.config, "")


if __name__ == '__main__':
    unittest.main()
