from bs4 import BeautifulSoup
import requests
import re
import lxml

"""
Okay so below you will see a bunch of for loops that are nested within each other.
Now, you might think that that provides a problem, because 3 nested for loops are O(n^3), 
but the way RSS feeds work means that technically this is just a O(n) algorithm
"""


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
        parse_value = find_parser(url_entry)
        response = requests.get(url_entry)
        soup = BeautifulSoup(response.content, parse_value)
        # print(soup.prettify())
        if soup.rss is not None:
            tag = soup.rss
            tag = tag.channel
            channel_dict = {"RSS_String": tag.title.string, "Link": tag.link.string}
            feed.append(channel_dict)
            for item in tag.find_all(re.compile("item")):
                feed_dict = {}
                for title in item.find_all(re.compile("title")):
                    for entry in title.find_all(string=True):
                        feed_dict["RSS_String"] = entry
                for link in item.find_all(re.compile("link")):
                    for entry in link.find_all(string=True):
                        feed_dict["Link"] = entry
                feed.append(feed_dict)
        elif soup.find_all(re.compile("atom")) is not None:
            tag = soup.feed
            for entry in tag.find_all("entry"):
                for title in entry.find_all("title"):
                    for string in title.find_all(string=True):
                        feed.append(string)
        feed = fix_feed(feed)
        total_feed = feed
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
    if len(response) <= 3:
        return "Invalid URL Length"
    test_string = (response[-3] + response[-2] + response[-1])
    if test_string == "tml":
        return "lxml"
    else:
        return "lxml-xml"


def fix_feed(feed):
    end_feed = []
    if len(feed) is None or len(feed) <= 0:
        return "ERROR: FEED IS EMPTY"
    for i in range(len(feed)):
        if i == 0:
            end_feed.append(feed[i])
        elif feed[i] == feed[i - 1]:
            continue
        else:
            end_feed.append(feed[i])
    return end_feed
