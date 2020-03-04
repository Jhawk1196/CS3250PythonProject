from atoma import *
from bs4 import BeautifulSoup
import requests
import lxml

def parse_feed(url):
    feed = parse_rss_file(url)
    print(feed.description)
    return feed

def url_check(url):
    url = str(url)
    if (len(url) >= 3):
        if (url[-3] + url[-2] + url[-1]) == "xml":
            return True

def test():
    print("Hello World")

def parse_xml_feed(xml_input):
    feed = parse_rss_file(xml_input)
    print(feed.description)
    return feed

def parse_url_feed(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    feed = soup.item.title.string
    return feed
