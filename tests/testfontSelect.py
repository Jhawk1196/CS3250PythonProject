import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font


class testFontSelect(unittest.TestCase):

    def testFontStyle(self):
        customfont = font.Font(family='Helvetica', size=12, weight="bold")
        self.assertEqual('Times', fontSelect.fontStyle(customfont, 'Times').cget("family"))

    def testFontSize(self):
        customfont = font.Font(family='Helvetica', size=12)
        self.assertEqual(16, fontSelect.fontSize(customfont, 16).cget("size"))

    def testFontColor(self):
        label = Message(fg='Red')
        self.assertEqual('Black', fontSelect.fontColor(label, 'Black').cget("fg"))
