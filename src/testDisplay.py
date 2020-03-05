import unittest
import src.display as display

class TestHelloWorld(unittest.TestCase):
    def test_Hello_World(self):
        self.assertEqual('Hello, world!', display.helloWorld('Hello, world!'))
    def test_Not_Hello_World(self):
        self.assertNotEqual('Hello, world!', display.helloWorld('Goodbye, earth!'))