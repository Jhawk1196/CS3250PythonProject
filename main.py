from src.display import helloWorld
from src.parser import parse_url_feed
from src.argument_parser import parse_args

args = parse_args()
# print(f"file is: {args.file}")
# print(f"url is: {args.url}")
#
# https://xkcd.com/atom.xml
# https://www.foxnews.com/politics.html

if args.url:
    feed = parse_url_feed(args.url)
elif args.file:
    feed = parse_url_feed(args.file)
else:
    feed = parse_url_feed("http://rss.cnn.com/rss/cnn_allpolitics.rss")

helloWorld(feed)
