import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font


class testFontSelect(unittest.TestCase):

    def testFontStyle(self):
        customfont = font.Font(family='Helvetica', size=12, weight="bold")
        self.assertEqual('Times', fontSelect.font_style(customfont, 'Times').cget("family"))

    def testFontSize(self):
        customfont = font.Font(family='Helvetica', size=12)
        self.assertEqual(16, fontSelect.font_size(customfont, 16).cget("size"))

    def testFontColor(self):
        label = Message(fg='Red')
        self.assertEqual('Black', fontSelect.font_color(label, 'Black').cget("fg"))
