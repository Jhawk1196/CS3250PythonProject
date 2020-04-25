"""
testParser.py

Used to test parser
"""
import unittest
from mock import Mock
import sys
import src.parser as parser

sys.modules['atoma'] = Mock()
sys.modules['requests'] = Mock()
sys.modules['lxml'] = Mock()
sys.modules['bs4'] = Mock()


# @patch('parser.bs4.BeautifulSoup')
class TestURLCheck(unittest.TestCase):
    def test_URL_Check_empty(self):
        self.assertFalse(parser.check_url(''))

    def test_URL_Check_notXML(self):
        self.assertFalse(parser.check_url('randomWords'))

    def test_URL_Check_endsinXML(self):
        self.assertTrue(parser.check_url('urlisxml'))

    def test_URL_Check_rss(self):
        self.assertTrue(parser.check_url('testingrss'))

    def test_URL_Check_incompat(self):
        self.assertFalse(parser.check_url('nevergonnagiveyouup'))

    def test_URL_Check_html(self):
        self.assertTrue(parser.check_url('urlishtml'))

    def test_URL_Check_FeedBurner(self):
        self.assertTrue(parser.check_url("http://feeds.feedburner.com/ign/all"))

    def test_URL_Check_Safe_FeedBurner(self):
        self.assertTrue(parser.check_url("https://feeds.feedburner.com/ign/all"))


class TestFindParser(unittest.TestCase):
    def test_find_parser_isXML(self):
        self.assertEqual(parser.find_parser("yayayayayyduasydiaifyaiyiafyaiyffaiyfxml"), "lxml-xml")

    def test_find_parser_isTML(self):
        self.assertEqual(parser.find_parser("sdasjhdadhausudhaudajdstml"), "lxml")

    def test_find_parser_isEmpty(self):
        with self.assertRaises(expected_exception=Exception):
            parser.find_parser("")


class TestParseUrl(unittest.TestCase):
    def test_parse_goodURL(self):
        self.assertIsNot(parser.parse_url_feed("http://rss.cnn.com/rss/cnn_allpolitics.rss"), "Invalid URL. Must Be a "
                                                                                              "RSS Feed URL ending in"
                                                                                              ".rss, .html, or .xml: "
                                                                                              "http://rss.cnn.com/rss"
                                                                                              "/cnn_allpolitics.rss")

    def test_parse_notNone(self):
        self.assertIsNotNone(parser.parse_url_feed("http://rss.cnn.com/rss/cnn_allpolitics.rss"))

    def test_parse_badURL(self):
        with self.assertRaises(expected_exception=Exception):
            parser.parse_url_feed("http://bad.url.notcorrect")

    def test_parse_returnsURLList(self):
        url_list = ["http://rss.cnn.com/rss/cnn_allpolitics.rss", "https://xkcd.com/atom.xml",
                    "http://feeds.feedburner.com/ign/all"]
        self.assertIsNotNone(parser.parse_url_feed(url_list))

    def test_parse_URLListHasBadURL(self):
        url_list = ["http://rss.cnn.com/rss/cnn_allpolitics.rss", "http://bad.url.notcorrect",
                    "https://xkcd.com/atom.xml", "http://feeds.feedburner.com/ign/all"]
        with self.assertRaises(expected_exception=Exception):
            parser.parse_url_feed(url_list)
