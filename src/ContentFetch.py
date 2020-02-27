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

import requests
import signal
from contextlib import contextmanager


class TimeoutException(Exception): pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)

    try:
        yield
    finally:
        signal.alarm(0)


def get_response(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    while True:
        try:
            # Waiting for 30 seconds to receive a response object
            with time_limit(30):
                # print(f"Requesting url data : {url}")
                content = requests.get(url, headers=hdr).content
                break
        except Exception as e:
            print('Request Timeout!!')
            raise e
        pass
    return content