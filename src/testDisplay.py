import unittest
import src.display as display


class TestHelloWorld(unittest.TestCase):
    def runTest(self):
        self.assertEqual('Hello, world!', display.helloWorld())
