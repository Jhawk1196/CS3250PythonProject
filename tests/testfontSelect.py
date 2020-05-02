import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font
from mock import patch


class TestFontStyle(unittest.TestCase):

    @patch('tkinter.font.Font', autospec=True)
    def test_calls_config(
            self, mock_font):
        """
        Test font_style method correctly called config to change font family
        """
        root = Tk()
        custom = mock_font(root, family='Helvetica', size=12)
        fontSelect.font_style(custom, 'Times')
        custom.config.assert_called_with(family='Times')

    def test_configs_font(
            self):
        """
        Test for font_style and font_size methods correctly changing
        appropriate attribute (family, size)
        """
        root = Tk()
        custom = font.Font(root, family='Helvetica', size=12)
        self.assertEqual(custom.cget('family'), 'Helvetica')
        fontSelect.font_style(custom, 'Times')
        self.assertEqual(custom.cget('family'), 'Times')
        fontSelect.font_size(custom, 18)
        self.assertEqual(custom.cget('size'), 18)

    def test_fontColor(
            self):
        """
        Test font_color method correctly changes fg attribute of Message
         called label
         """
        root = Tk()
        label = Message(root, fg='Red')
        label.pack()
        self.assertEqual('Black', fontSelect.font_color(label, 'Black')
                         .cget("fg"))
