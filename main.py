
#from src.display import displayView

from src.display import display

from src.argument_parser import parse_args

args = parse_args()
# print(f"file is: {args.file}")
# print(f"url is: {args.url}")
# http://rss.cnn.com/rss/cnn_allpolitics.rss
# https://xkcd.com/atom.xml
# https://www.foxnews.com/politics.html
# http://feeds.feedburner.com/ign/all


display(args)
