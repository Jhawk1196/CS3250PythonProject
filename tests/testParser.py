import unittest
from mock import Mock
import sys
import src.parser as parser

sys.modules['atoma'] = Mock()
sys.modules['requests'] = Mock()
sys.modules['lxml'] = Mock()
sys.modules['bs4'] = Mock()


class TestURLCheck(unittest.TestCase):
    def test_URL_Check_empty(
            self):
        """
        Asserts that an empty url will return a Boolean false
        """
        self.assertFalse(parser.check_url(''))

    def test_URL_Check_notXML(
            self):
        """
        Asserts that a string url not ending in 'xml' will return a boolean
        false
        """
        self.assertFalse(parser.check_url('randomWords'))

    def test_URL_Check_endsinXML(
            self):
        """
        Asserts that a string url ending in 'xml' will return Boolean true
        """
        self.assertTrue(parser.check_url('urlisxml'))

    def test_URL_Check_rss(
            self):
        """
        Asserts that a string url ending in rss will return Boolean true
        """
        self.assertTrue(parser.check_url('testingrss'))

    def test_URL_Check_incompatible(
            self):
        """
        Asserts that an improperly formatted url will return a Boolean false
        """
        self.assertFalse(parser.check_url('nevergonnagiveyouup'))

    def test_URL_Check_html(
            self):
        """
        Asserts that a string url ending in html will return boolean True
        """
        self.assertTrue(parser.check_url('urlishtml'))

    def test_URL_Check_FeedBurner(
            self):
        """
        Asserts that a string url starting with 'http' and containing the word
        'feeds' will return boolean true
        """
        self.assertTrue(parser.check_url(
            "http://feeds.feedburner.com/ign/all"))

    def test_URL_Check_Safe_FeedBurner(
            self):
        """
        Asserts that a string url starting with 'https' and containing the word
         'feeds' will return boolean true
        """
        self.assertTrue(parser.check_url(
            "https://feeds.feedburner.com/ign/all"))


class TestFindParser(unittest.TestCase):
    def test_find_parser_isXML(
            self):
        """
        Asserts find_parser method will return 'lxml-xml' if the string passed
        to method ends in xml
        """
        self.assertEqual(parser.find_parser(
            "yayayayayyduasydiaifyaiyiafyaiyffaiyfxml"), "lxml-xml")

    def test_find_parser_isTML(
            self):
        """
        Asserts find_parser method will return 'lxml-xml' if the string passed
        to method ends in 'tml'
        """
        self.assertEqual(parser.find_parser("sdasjhdadhausudhaudajdstml"),
                         "lxml")

    def test_find_parser_isEmpty(
            self):
        """
        Asserts that an empty string passed to find_parser method throws
        and exception
        """
        with self.assertRaises(expected_exception=Exception):
            parser.find_parser("")


class TestParseUrl(unittest.TestCase):
    def test_parse_goodURL(
            self):
        """
        Asserts that an appropriately formatted url feed (linked list)
        passed to parse_url_feed will not return string citing failure
        conditions
        """
        self.assertIsNot(parser.parse_url_feed(
            "http://rss.cnn.com/rss/cnn_allpolitics.rss"),
            "Invalid URL. Must Be a RSS Feed URL ending in .rss, .html, or "
            ".xml: http://rss.cnn.com/rss/cnn_allpolitics.rss")

    def test_parse_notNone(
            self):
        """
        Asserts that an appropriately formatted url feed (linked list)
        passed to parse_url_feed does not return nothing
        """
        self.assertIsNotNone(parser.parse_url_feed("http://rss.cnn.com/rss/"
                                                   "cnn_allpolitics.rss"))

    def test_parse_badURL(
            self):
        """
        Asserts that an inappropriately formatted url feed (linked list)
        passed to parse_url_feed will raise an exception
        """
        with self.assertRaises(expected_exception=Exception):
            parser.parse_url_feed("http://bad.url.notcorrect")

    def test_parse_returnsURLList(
            self):
        """
        Asserts that an appropriately formatted url feed (linked list)
        passed to parse_url_feed will not return nothing
        """
        url_list = ["http://rss.cnn.com/rss/cnn_allpolitics.rss",
                    "https://xkcd.com/atom.xml",
                    "http://feeds.feedburner.com/ign/all"]
        self.assertIsNotNone(parser.parse_url_feed(url_list))

    def test_parse_URLListHasBadURL(
            self):
        """
        Asserts that a linked list containing an inappropriately formatted
        passed to method parse_url_feed will raise an exception
        """
        url_list = ["http://rss.cnn.com/rss/cnn_allpolitics.rss",
                    "http://bad.url.notcorrect",
                    "https://xkcd.com/atom.xml",
                    "http://feeds.feedburner.com/ign/all"]
        with self.assertRaises(expected_exception=Exception):
            parser.parse_url_feed(url_list)


class TestTruncate(unittest.TestCase):
    def test_input_lessThan80(
            self):
        """
        Asserts that the method truncate does not remove any characters in a
        string length less than 80 characters
        """
        self.assertEqual(parser.truncate("a"), "a")
        self.assertEqual(parser.truncate("abcdefghijklmnopqrstuvwxyz"),
                         "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(parser.truncate("ThisLineContains79CharactersThisLine"
                                         "Contains79CharactersThisLineContains"
                                         "79Chara"),
                         "ThisLineContains79CharactersThisLineContains79"
                         "CharactersThisLineContains79Chara")

    def test_input_greaterThan80(
            self):
        """
        Asserts that the method truncate removes characters from a string over
        79 characters in length and adds and ellipsis
        """
        self.assertEqual(parser.truncate("ThisLineContains84CharactersThisLine"
                                         "Contains84CharactersThisLineContains"
                                         "84Characters"),
                         "ThisLineContains84CharactersThisLineContains84"
                         "CharactersThisLineContains84Chara...")
