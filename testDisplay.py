import unittest
import src.display as display


class TestHelloWorld(unittest.TestCase):
    def runTest(self):
        self.assertEqual("xkcd.com", display.helloWorld("http://xkcd.com/atom.xml"))
