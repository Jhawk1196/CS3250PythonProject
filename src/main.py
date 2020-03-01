"""
***WILL BE REMOVED IN DUE TIME. STRICTLY USED FOR REFERENCE***
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

from src.DataParser import get_soup, parse_record
from src.db_connect import get_connection, get_max_records, execute_query
from apscheduler.schedulers.blocking import BlockingScheduler
from tkinter import ttk

# from apscheduler.schedulers.background import BackgroundScheduler

# get_max_query = 'SELECT COALESCE(max(itunes_episode),0) FROM tasteofindia.posts;'
# query_string = 'INSERT INTO tasteofindia.{0} ({1}) VALUES ({2}{3});'

"""
col_list = {
    'posts'	: ['itunes_episode' ,'title' ,'link' ,'enclosure_url' ,'enclosure_type' ,'enclosure_length' ,'guid'
              ,'guid_isPermaLink' ,'dc_creator' ,'media_rights' ,'pubDate'] ,'itunes_data'	: ['episode','ti tle','im age_link','du ration','ex plicit','ep isodeType','au thor','su btitle','su
                      mmary']
    ,'me dia'		: ['itunes_episode',' url',' type',' duration',' lang',' medium']
}
query_strings	= {k: query_string.format(k , ','.join(col_list[k]),( '%s,'* ( len(col_list[k])- 1 ) ), '%s') for k in
                 col_list}
"""


def persist_record(conn, data, tb_name):
    """
        Format the query parameter script and records it in DB
    """
    query_param = tuple(list(map(lambda k: data[k], col_list[tb_name])))
    execute_query(conn, query_strings[tb_name], query_param)
    return


def persist_taste_of_india_record(conn, data):
    """
    """
    persist_record(conn, data, 'posts')
    persist_record(conn, data['itunes'], 'itunes_data')
    for media in data['media']:
        persist_record(conn, media, 'media')

    conn.commit()
    return True


def process_records(content, conn):
    record_count = len(content)

    current_max = get_max_records(conn, get_max_query)
    print('Current Max : ', current_max)

    records = {}

    if record_count == current_max:
        print("No new records found!!")
        return records

    print(f"Total Records Found: {record_count}. Currently present: {current_max}")

    [persist_taste_of_india_record(conn, record) for record in
     map(parse_record, content[record_count - current_max - 1::-1])]

    # for data in map(parse_record,content[record_count-current_max-1::-1]):
    # records[int(data['itunes']['episode'])] = data

    # for k in sorted(records):
    # print(k)

    return records


def update_feed_data(feed, conn):
    content = get_soup(feed)

    print(f"Processing Records for : {feed}")
    records = content.find_all('item')

    process_records(records, conn)

    # store_tags(records)
    return


def begin(feed_url, db_credential_file):
    try:
        connection = get_connection(db_credential_file)
        update_feed_data(feed_url, connection)
    except Exception as e:
        print('Error Received...')
        print(e)
    finally:
        print('Closing connection')
        connection.close()


if __name__ == '__main__':

    feed_url =""
    db_credentials = 'connection.json'

    print('Main Script Running...')

    begin(feed_url, db_credentials)

    scheduler = BlockingScheduler()
    # scheduler	= BackgroundScheduler()
    scheduler.add_job(begin, 'interval', [feed_url, db_credentials], hours=12)

    try:
        scheduler.start()
    except Exception as e:
        print('Stopping Schedule!!')

    print('Main Script Exiting!!')
