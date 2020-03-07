from src.display import helloWorld
from src.parser import parse_url_feed
from argument_parser import parse_args

args = parse_args()
# print(f"file is: {args.file}")
# print(f"url is: {args.url}")

if args.url:
    feed = parse_url_feed(args.url)
elif args.file:
    feed = parse_url_feed(args.file)
else:
    feed = parse_url_feed("http://xkcd.com/atom.xml")

helloWorld(feed)
