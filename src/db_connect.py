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

import psycopg2
import json


def get_connection(file):
    with open(file) as inFile:
        creds = json.load(inFile)

    database = creds['database']
    user = creds['user']
    password = creds['password']
    host = creds['host']
    port = creds['port']

    connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    return connection


def get_max_records(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        record = cursor.fetchone()
        print('Record received: ', record)
    finally:
        cursor.close()
    return record[0]


def execute_query(conn, query, params):
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
    except Exception as e:
        raise e
    finally:
        cursor.close()


if __name__ == '__main__':
    get_max_query = 'SELECT COALESCE(max(episode),0) FROM tasteofindia.itunes_data;'
    conn = get_connection('connection.json')
    print(get_max_records(conn, get_max_query))
