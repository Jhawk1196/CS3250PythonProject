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

    def test_ParseURLFeed_false(self):
        self.assertEqual(parser.parse_url_feed('randomwords'),
                         "Invalid URL. Must Be a RSS Feed URL ending in .rss, .html, or .xml")

    def test_URL_Check_incompat(self):
        self.assertFalse(parser.check_url('nevergonnagiveyouup'))


class TestFindParser(unittest.TestCase):
    def test_find_parser_isXML(self):
        self.assertEqual(parser.find_parser("yayayayayyduasydiaifyaiyiafyaiyffaiyfxml"), "lxml-xml")

    def test_find_parser_isTML(self):
        self.assertEqual(parser.find_parser("sdasjhdadhausudhaudajdstml"), "lxml")

    def test_find_parser_isEmpty(self):
        self.assertEqual(parser.find_parser(""), "Invalid URL Length")


class TestFixFeed(unittest.TestCase):
    def test_fix_feed_isEmpty(self):
        feed = []
        self.assertEqual(parser.fix_feed(feed), "ERROR: FEED IS EMPTY")

    def test_fix_feed_isString(self):
        feed = ["Hello", "Hello"]
        fixed_feed = ["Hello"]
        self.assertEqual(parser.fix_feed(feed), fixed_feed)

    def test_fix_feed_isDict(self):
        feed = [{"Hello": "World"}, {"Hello": "World"}, {"Wonderful": "Day"}]
        fixed_feed = [{"Hello": "World"}, {"Wonderful": "Day"}]
        self.assertEqual(parser.fix_feed(feed), fixed_feed)

    def test_fix_feed_isList(self):
        feed = [["Hello World", "What a Wonderful Day"], ["Hello World", "What a Wonderful Day"]]
        fixed_feed = [["Hello World", "What a Wonderful Day"]]
        self.assertEqual(parser.fix_feed(feed), fixed_feed)
