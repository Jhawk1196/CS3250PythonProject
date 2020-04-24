import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font
from os import environ
from mock import Mock, patch, MagicMock


class test_fontStyle(unittest.TestCase):
    @patch('tkinter.font.Font', autospec=True)
    def test_calls_config(self, mock_font):
        root = Tk()
        custom = mock_font(root, family='Helvetica', size=12)
        fontSelect.font_style(custom, 'Times')
        custom.config.assert_called_with(family='Times')

    def test_configs_font(self):
        root = Tk()
        custom = font.Font(root, family='Helvetica', size=12)
        self.assertEqual(custom.cget('family'), 'Helvetica')
        fontSelect.font_style(custom, 'Times')
        self.assertEqual(custom.cget('family'), 'Times')
        fontSelect.font_size(custom, 18)
        self.assertEqual(custom.cget('size'), 18)

    def testFontColor(self):
        root = Tk()
        label = Message(root, fg='Red')
        label.pack()
        self.assertEqual('Black', fontSelect.font_color(label, 'Black').cget("fg"))
