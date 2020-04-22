from src.argument_parser import parse_args
from src.display import display

args = parse_args()
# http://rss.cnn.com/rss/cnn_allpolitics.rss
# https://xkcd.com/atom.xml
# https://www.foxnews.com/politics.html
# http://feeds.feedburner.com/ign/all


display(args)
