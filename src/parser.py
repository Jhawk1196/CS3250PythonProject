from atoma import *


def parse_feed(url):
    feed = parse_rss_file(url)
    print(feed.description)
    return feed


def url_check(url):
    url = str(url)
    if (url[-3] + url[-2] + url[-1]) == "xml":
        return True


def test():
    print("Hello World")