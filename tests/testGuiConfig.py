import unittest
import sys
import os
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
        """
        Test GUI correctly loads saved config data for GUI background color
        """
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.background_color, 'black')

    def test_font(
            self):
        """
        Test GUI correctly loads saved config data for font style (family)
        """
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_family, 'Helvetica')

    def test_time(
            self):
        """
        Test GUI correctly loads saved config data for cycle time between feeds
        """
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(config.time, 5000)

    def test_window_placement(
            self):
        """
        Test GUI correctly loads saved config data for the window placement
        """
        sys.argv[1:] = ["--config", "default_config.yml"]
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        self.assertEqual(str(config.window_placement), "800x50+0+25")


    def test_can_change(
            self):

        """
        Tests that the correct defaults are loaded if no .yml file is provided
        """
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        config.font_color = 'black'
        config.background_color = 'white'
        self.assertEqual(config.font_color, "black")
        self.assertEqual(config.background_color, "white")


class TestSaveLoad(unittest.TestCase):
    def test_save_load(self):
        """
        Tests that saved configurations are loaded again
        """
        args = argument_parser.parse_args()
        config = gui_config.Configuration(args)
        config.font_color = 'black'
        save_info = {}
        save_info['font_color'] = config.font_color
        config.save_configuration(save_info)

        sys.argv[1:] = ["--config", "src/saved_config.yml"]
        args = argument_parser.parse_args()
        os.remove("src/saved_config.yml")
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_color, "white")

class TestArgs(unittest.TestCase):
    def test_some_stuff(self):
        args = argument_parser.parse_args()
        args.config = ["default_config.yml"]
        config = gui_config.Configuration(args)
        self.assertEqual(config.font_color, 'white')