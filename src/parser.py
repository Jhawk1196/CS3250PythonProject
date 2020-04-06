from bs4 import BeautifulSoup
import requests
import re
import lxml


def parse_url_feed(url):
    feed = []
    total_feed = []
    url_list = []
    if isinstance(url, str):
        url_list.append(url)
    elif isinstance(url, list):
        url_list = url
    for url_entry in url_list:
        if not check_url(url_entry):
            return "Invalid URL. Must Be a RSS Feed URL ending in .rss, .html, or .xml"
        response = requests.get(url_entry)
        parse_value = find_parser(response)
        soup = BeautifulSoup(response.content, parse_value)
        # print(soup.prettify())
        if soup.rss is not None:
            tag = soup.rss
            tag = tag.channel
            for title in tag.find_all(re.compile("title")):
                for entry in title.find_all(string=True):
                    feed.append(entry)
        elif soup.find_all(re.compile("atom")) is not None:
            tag = soup.feed
            for entry in tag.find_all("entry"):
                for title in entry.find_all("title"):
                    for string in title.find_all(string=True):
                        feed.append(string)
        feed = fix_feed(feed)
        total_feed.append(feed)
    return total_feed


def check_url(url):
    url = str(url)
    if len(url) == 0:
        return False
    test_string = (url[-3] + url[-2] + url[-1])
    second_test_string = ""
    if len(url) > 11:
        second_test_string = (url[7] + url[8] + url[9] + url[10] + url[11])
    if test_string == "rss":
        return True
    elif test_string == "xml":
        return True
    elif test_string == "tml":
        return True
    elif second_test_string == "feeds":
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


def fix_feed(feed):
    end_feed = []
    for i in range(len(feed)):
        if i == 0:
            end_feed.append(feed[i])
        elif feed[i] == feed[i - 1]:
            continue
        else:
            end_feed.append(feed[i])
    return end_feed
