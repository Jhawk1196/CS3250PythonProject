"""
This code was copied, with some modifications, from the GitHub user vintageplayer
from https://github.com/vintageplayer/RSS-Parser

MIT License

Copyright (c) 2019 Aditya Agarwal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from bs4 import BeautifulSoup
from src.ContentFetch import get_response


def get_soup(url):
    response = get_response(url)
    soup = BeautifulSoup(response, 'lxml-xml')
    return soup


def parse_record(record):
    details = {}

    try:
        details['title'] = record.find('title').text
    except Exception as e:
        details['title'] = None

    try:
        details['link'] = record.find('link').text
    except Exception as e:
        details['link'] = None

    try:
        details['enclosure_url'] = record.find('enclosure')['url']
    except Exception as e:
        details['enclosure_url'] = None

    try:
        details['enclosure_type'] = record.find('enclosure')['type']
    except Exception as e:
        details['enclosure_type'] = None

    try:
        details['enclosure_length'] = record.find('enclosure')['length']
    except Exception as e:
        details['enclosure_length'] = None

    try:
        details['guid'] = record.find('guid').text
    except Exception as e:
        details['guid'] = None

    try:
        details['guid_isPermaLink'] = record.find('guid')['isPermaLink']
    except Exception as e:
        details['guid_isPermaLink'] = None

    try:
        details['dc_creator'] = record.find('dc:creator').text
    except Exception as e:
        details['dc_creator'] = None

    try:
        details['media_rights'] = record.find('media:rights')['status']
    except Exception as e:
        details['media_rights'] = None

    try:
        details['pubDate'] = record.find('pubDate').text
    except Exception as e:
        details['pubDate'] = None

    try:
        details['content_encoded']	= record.find('content:encoded').text
    except Exception as e: \
        details['content_encoded'] = None

    return details


def store_tags(content):
    tag_set = set()

    for post in content[:1]:
        # tag_set = tag_set | set([content.name for content in post.find_all()])
        # print([content.attrs for content in post.find_all()])
        for element in post.find_all():
            if element.attrs:
                tag_set = tag_set | set([f"{element.name}:{attr}" for attr in element.attrs])
            tag_set.add(element.name)
    print(tag_set)

    with open('tag_list.txt', 'w') as f:
        for tag in tag_set:
            # tag = re.sub('[:]','_',tag)
            f.write(f"{tag}\n")

    return tag_set


def get_tags(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def check_tags():
    tag_set = set()
    tag_file = 'tag_list.txt'
    tags_list = get_tags(tag_file)

    for post in content[current_max:current_max + 10]:
        tags = [content.name for content in post.find_all()]
        print((set(tags) - tag_set) | (tag_set - set(tags)))
        print(post.find('title').text)

        for tag in tags_list:
            try:
                line = f"{tag} : {post.find(tag).text}"
            except Exception as e:
                print(f"{tag} NOT found")
        print(tags)
        print(tags_list)