"""
Ok, Time to rewrite all of this....
"""

from src.display import helloWorld
from src.parser import parse_url_feed

feed = parse_url_feed("http://rss.cnn.com/rss/cnn_us.rss")

helloWorld(feed)