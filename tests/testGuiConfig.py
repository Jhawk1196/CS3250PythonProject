import unittest
import sys
import src.gui_config as gui_config
import src.argument_parser as argument_parser


class TestLoadsDefault(unittest.TestCase):
    def test_font_size(
            self):
        """Test GUI correctly loads saved config data for font size"""
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_size, 15)

    def test_font_color(
            self):
        """Test GUI correctly loads saved config data for font color"""
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_color, 'white')

    def test_bg_color(
            self):
        """Test GUI correctly loads saved config data for GUI background color"""
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.background_color, 'black')

    def test_font(
            self):
        """Test GUI correctly loads saved config data for font style (family)"""
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_family, 'Helvetica')

    def test_time(
            self):
        """Test GUI correctly loads saved config data for cycle time between feeds"""
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.time, 5000)


class TestSavesAndLoads(unittest.TestCase):
    pass
