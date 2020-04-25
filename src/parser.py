from bs4 import BeautifulSoup
import requests
import re
import typing
import lxml

"""
Okay so below you will see a bunch of for loops that are nested within each other.
Now, you might think that that provides a problem, because 3 nested for loops are O(n^3), 
but the way RSS feeds work means that technically this is just a O(n) algorithm
"""


class Node:  # pragma: no cover
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:  # pragma: no cover
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        elif self.tail.data == item:
            return
        else:
            self.tail.next = item

        self.tail = item


def parse_url_feed(incoming) -> typing.Union[list, str]:
    total_feed = LinkedList()
    url_list = return_list(incoming)
    for url_entry in url_list:
        if not check_url(url_entry):
            raise Exception("Invalid URL. Must Be a RSS Feed URL ending in .rss, .html, or .xml: " + url_entry)
        parse_value = find_parser(url_entry)
        response = requests.get(url_entry)
        soup = BeautifulSoup(response.content, parse_value)
        if soup.rss is not None:
            feed = rss_parse(soup)
            total_feed.add_list_item(feed)
        elif soup.find_all(re.compile("atom.xml")) is not None:
            feed = atom_parse(soup)
            total_feed.add_list_item(feed)
    return total_feed


def check_url(url: str):
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


def find_parser(response: str) -> str:
    if len(response) <= 3:
        raise Exception("Invalid URL Length")
    test_string = (response[-3] + response[-2] + response[-1])
    if test_string == "tml":
        return "lxml"
    else:
        return "lxml-xml"


def return_list(incoming) -> list:
    url_list = []
    if isinstance(incoming, str):
        url_list.append(incoming)
    elif isinstance(incoming, list):
        url_list = incoming
    return url_list


def rss_parse(soup: BeautifulSoup) -> LinkedList:
    feed = LinkedList()
    tag = soup.rss
    tag = tag.channel
    channel_dict = {"RSS_String": tag.title.string, "Link": tag.link.string}
    feed.add_list_item(channel_dict)
    for item in tag.find_all(re.compile("item")):
        feed_dict = {}
        for title in item.find_all(re.compile("title")):
            for entry in title.find_all(string=True):
                feed_dict["RSS_String"] = entry
        for link in item.find_all(re.compile("link")):
            for entry in link.find_all(string=True):
                feed_dict["Link"] = entry
        feed.add_list_item(feed_dict)
    return feed


def atom_parse(soup: BeautifulSoup) -> LinkedList:
    feed = LinkedList()
    tag = soup.feed
    for entry in tag.find_all("entry"):
        feed_dict = {}
        for title in entry.find_all("title"):
            for string in title.find_all(string=True):
                feed_dict["RSS_String"] = string
        for link in entry.find_all(re.compile("link")):
            feed_dict["Link"] = link.get('href')
        feed.add_list_item(feed_dict)
    return feed
