import unittest
from tkinter import *
import src.fontSelect as fontSelect
from tkinter import font
from src import display
from mock import Mock, patch, MagicMock


class testFontSelect(unittest.TestCase):

    def testFontStyle(self):
        root = Tk()
        customfont = font.Font(root=root, family='Helvetica')
        fontSelect.fontStyle(customfont, 'Times')
        self.assertEqual('Times', customfont.cget('family'))

    def testFontSize(self):
        root = Tk()
        customfont = font.Font(root=root, family='Helvetica', size=12)
        self.assertEqual(16, fontSelect.fontSize(customfont, 16).cget("size"))

    def testFontColor(self):
        root = Tk()
        label = Message(master=root, fg='Red')
        label.pack()
        self.assertEqual('Black', fontSelect.fontColor(label, 'Black').cget("fg"))
