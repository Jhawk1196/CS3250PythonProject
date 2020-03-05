from bs4 import BeautifulSoup
import requests
import lxml


def parse_url_feed(url):
    if not check_url(url):
        return "Invalid URL. Must Be a RSS Feed URL ending in .rss, .html, or .xml"
    response = requests.get(url)
    parse_value = find_parser(response)
    soup = BeautifulSoup(response.content, parse_value)
    # print(soup.prettify())
    feed = soup.title.string
    return feed


def check_url(url):
    url = str(url)
    if len(url) == 0:
        return False
    test_string = (url[-3] + url[-2] + url[-1])
    if test_string == "rss":
        return True
    elif test_string == "xml":
        return True
    else:
        return False


def find_parser(response):
    test_url = response.url
    test_string = (test_url[-3] + test_url[-2] + test_url[-1])
    if test_string == "tml":
        return "lxml"
    else:
        return "lxml-xml"
