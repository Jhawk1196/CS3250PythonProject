import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font


class testFontSelect(unittest.TestCase):

    def testFontStyle(self):
        customfont = font.Font(family='Helvetica', size=12, weight="bold")
        fontSelect.fontStyle(customfont, 'Times')
        self.assertEqual('Times', customfont.cget("family"))

    def testFontSize(self):
        customfont = font.Font(family='Helvetica', size=12)
        fontSelect.fontSize(customfont, 16)
        self.assertEqual(16, customfont.cget("size"))

    def testFontColor(self):
        label = Message(fg='Red')
        fontSelect.fontColor(label, 'Black')
        self.assertEqual(label.cget("fg"), 'Black')