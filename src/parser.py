from atoma import *
from bs4 import BeautifulSoup
import requests
import lxml


def parse_xml_feed(xml_input):
    feed = parse_rss_file(xml_input)
    print(feed.description)
    return feed

def parse_url_feed(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    feed = soup.item.title.string
    return feed