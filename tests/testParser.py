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
