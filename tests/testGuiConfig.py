import unittest
from mock import Mock
import sys
import src.gui_config as gui_config
import src.argument_parser as argument_parser


class TestLoadsDefault(unittest.TestCase):
    # test to make sure it loads the default configuration appropriately
    def test_font_size(self):
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_size, 15)

    def test_font_color(self):
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_color, 'white')

    def test_bg_color(self):
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.background_color, 'black')

    def test_font(self):
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_family, 'Helvetica')

    def test_time(self):
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.time, 5000)


class TestSavesAndLoads(unittest.TestCase):
    pass
