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
        self.assertFalse(parser.check_url(''))

    def test_URL_Check_notXML(self):
        self.assertFalse(parser.check_url('randomWords'))

    def test_URL_Check_endsinXML(self):
        self.assertTrue(parser.check_url('urlisxml'))
