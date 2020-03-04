import unittest
from display import *

class test_helloWorld(unittest.TestCase):
    def runTest(self):
        self.assertEqual('Hello, world!', helloWorld())
