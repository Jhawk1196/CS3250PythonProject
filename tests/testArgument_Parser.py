import unittest
import sys
import src.argument_parser as argument_parser


class TestURL(unittest.TestCase):
    def test_single_url(
            self):
        """Test for only url property of command line arguments"""
        test_check = "google.com"
        sys.argv[1:] = ["--url", test_check]
        args = argument_parser.parse_args()
        self.assertEqual(args.url, [test_check])
        self.assertEqual(args.file, None)
        self.assertEqual(args.config, "")

    def test_single_file(
            self):
        """Test for only file property of command line arguments"""
        sys.argv[1:] = ["--file", "some_file.json"]
        args = argument_parser.parse_args()
        self.assertEqual(args.file, ['some_file.json'])
        self.assertEqual(args.url, None)
        self.assertEqual(args.config, "")

    def test_single_config(
            self):
        """Test for only configuration file property of command line arguments"""
        sys.argv[1:] = ["--config", "some_config.yaml"]
        args = argument_parser.parse_args()
        self.assertEqual(args.config, ['some_config.yaml'])
        self.assertEqual(args.url, None)
        self.assertEqual(args.file, None)

    def test_multiple_url(
            self):
        """Test for multiple url properties of command line arguments"""
        test_check1 = "google.com"
        test_check2 = "duckduckgo.com"
        sys.argv[1:] = ["--url", test_check1, test_check2]
        args = argument_parser.parse_args()
        self.assertEqual(args.url, [test_check1, test_check2])
        self.assertEqual(args.file, None)
        self.assertEqual(args.config, "")

    def test_urls_and_files(
            self):
        """ Test for multiple urls and file properties of command line arguments"""
        url_check1 = "google.com"
        url_check2 = "duckduckgo.com"
        file_check1 = "some_file.json"
        file_check2 = "another_file.json"
        sys.argv[1:] = ["--url", url_check1, url_check2, "--file", file_check1, file_check2]
        args = argument_parser.parse_args()
        self.assertEqual(args.url, [url_check1, url_check2])
        self.assertEqual(args.file, [file_check1, file_check2])
        self.assertEqual(args.config, "")
