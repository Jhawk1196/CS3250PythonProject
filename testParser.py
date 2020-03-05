import unittest
from mock import Mock
import sys
import src.parser as parser

sys.modules['atoma'] = Mock()
sys.modules['requests'] = Mock()
sys.modules['lxml'] = Mock()
sys.modules['bs4'] = Mock()


# @patch('parser.bs4.BeautifulSoup')
class test_URL_Check(unittest.TestCase):
    def test_URL_Check_empty(self):
        self.assertFalse(parser.url_check(''))

    def test_URL_Check_notXML(self):
        self.assertFalse(parser.url_check('randomWords'))

    def test_URL_Check_endsinXML(self):
        self.assertTrue(parser.url_check('urlisxml'))
