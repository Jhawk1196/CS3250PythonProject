import unittest
import src.display as display

class TestHelloWorld(unittest.TestCase):
    def runTest(self):
        self.assertEqual("https://xkcd.com/atom.xml", display.helloWorld("https://xkcd.com/atom.xml"))