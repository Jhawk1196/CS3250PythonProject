"""
Parser.py

Used to parse URLs into a linked list of dictionaries.
"""

from bs4 import BeautifulSoup
import requests
import re


class Node:  # pragma: no cover
    """
    Creates a Node that contains data, and a next node
    Data holds any object.
    Next points to the next node, and should always be a node.
    """

    def __init__(
            self, data):
        """Initialize Node Class"""
        self.data = data
        self.next = None


class LinkedList:  # pragma: no cover
    """
    Creates a Linked List, with a head, and a tail.
    Head only contains the first link in the list, and should be called at the
    beginning of scan.
    Tail only contains the last link in the list, and should not be called.
    """

    def __init__(
            self):
        """Initialize Linked List Class"""
        self.head = None
        self.tail = None

    def add_list_item(
            self, item):
        """Add an item to the Linked List"""
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        elif self.tail.data == item:
            return
        else:
            self.tail.next = item

        self.tail = item


def parse_url_feed(
        incoming) -> LinkedList:
    """
    Receives either a list of URLs or a single URL, and returns a Linked
    List of Dictionaries
    """
    total_feed = LinkedList()
    url_list = return_list(incoming)
    for url_entry in url_list:
        if not check_url(url_entry):
            raise Exception("Invalid URL. Must Be a RSS Feed URL ending in "
                            ".rss, .html, or .xml: " + url_entry)
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


def check_url(
        url: str) -> bool:
    """Checks to see if the URL given is parseable"""
    url = str(url)
    if len(url) == 0:
        return False
    result1 = re.search("rss?", url)
    result2 = re.search("xml?", url)
    result3 = re.search("tml?", url)
    result4 = re.search("feeds?", url)
    if result1 is not None:
        return True
    elif result2 is not None:
        return True
    elif result3 is not None:
        return True
    elif result4 is not None:
        return True
    else:
        return False


def find_parser(
        response: str) -> str:
    """Checks to see which parser to use"""
    if len(response) <= 3:
        raise Exception("Invalid URL Length")
    result = re.search("tml?", response)
    if result is not None:
        return "lxml"
    else:
        return "lxml-xml"


def return_list(
        incoming) -> list:
    """
    Checks to see if incoming is a String or a List. If a String, adds the
    string to a list and returns.
    """
    url_list = []
    if isinstance(incoming, str):
        url_list.append(incoming)
    elif isinstance(incoming, list):
        url_list = incoming
    return url_list


def rss_parse(
        soup: BeautifulSoup) -> LinkedList:  # pragma: no cover
    """
    When URL is an RSS feed, returns a linked list of dictionaries
    containing the titles and links
    """
    feed = LinkedList()
    tag = soup.rss
    tag = tag.channel
    channel_dict = {"RSS_String": tag.title.string, "Link": tag.link.string}
    feed.add_list_item(channel_dict)
    for item in tag.find_all(re.compile("item?")):
        feed_dict = {}
        for title in item.find_all(re.compile("title?")):
            for entry in title.find_all(string=True):
                feed_dict["RSS_String"] = entry
                feed_dict["RSS_String"] = truncate(feed_dict["RSS_String"])
        for link in item.find_all(re.compile("link?")):
            for entry in link.find_all(string=True):
                feed_dict["Link"] = entry
        feed.add_list_item(feed_dict)
    return feed


def atom_parse(
        soup: BeautifulSoup) -> LinkedList:  # pragma: no cover
    """
    When URL is an Atom feed, returns a linked list of dictionaries containing
    the titles and links
    """
    feed = LinkedList()
    tag = soup.feed
    for entry in tag.find_all("entry"):
        feed_dict = {}
        for title in entry.find_all("title"):
            for string in title.find_all(string=True):
                feed_dict["RSS_String"] = string
                feed_dict["RSS_String"] = truncate(feed_dict["RSS_String"])
        for link in entry.find_all(re.compile("link?")):
            feed_dict["Link"] = link.get('href')
        feed.add_list_item(feed_dict)
    return feed


def truncate(
        input_line: str) -> str:
    """
    When a string is over 80 characters long, string is limited to 79
    characters for readability in GUI window, An ellipsis (...) is added to
    denote unseen text
    """
    if len(input_line) >= 80:
        input_line = input_line[0:79]
        return input_line + "..."
    else:
        return input_line
