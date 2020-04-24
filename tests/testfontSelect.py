import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font
import os
from src import display
from mock import Mock, patch, MagicMock


class testFontSelect(unittest.TestCase):

    def testFontStyle(self):
        if os.environ.get('DISPLAY', '') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        root = Tk()
        customfont = font.Font(root, family='Helvetica')
        fontSelect.font_style(customfont, 'Times')
        self.assertEqual('Times', customfont.cget('family'))

    def testFontSize(self):
        root = Tk()
        customfont = font.Font(root, family='Helvetica', size=12)
        self.assertEqual(16, fontSelect.font_size(customfont, 16).cget("size"))

    def testFontColor(self):
        root = Tk()
        label = Message(root, fg='Red')
        label.pack()
        self.assertEqual('Black', fontSelect.font_color(label, 'Black').cget("fg"))
