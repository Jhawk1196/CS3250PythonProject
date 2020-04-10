import unittest
from mock import Mock
import sys

sys.modules['atoma'] = Mock()
sys.modules['requests'] = Mock()
sys.modules['lxml'] = Mock()
sys.modules['bs4'] = Mock()

import src.parser as parser

# @patch('parser.bs4.BeautifulSoup')
class test_URL_Check(unittest.TestCase):
    def test_URL_Check_empty(self):
        self.assertFalse(parser.check_url(''))

    def test_URL_Check_notXML(self):
        self.assertFalse(parser.check_url('randomWords'))

    def test_URL_Check_endsinXML(self):
        self.assertTrue(parser.check_url('urlisxml'))

    def test_URL_Check_rss(self):
        self.assertTrue(parser.check_url('testingrss'))

    def test_ParseURLFeed_false(self):
        self.assertEqual(parser.parse_url_feed('randomwords'), "Invalid URL. Must Be a RSS Feed URL ending in .rss, .html, or .xml")

    def test_URL_Check_incompat(self):
        self.assertFalse(parser.check_url('nevergonnagiveyouup'))