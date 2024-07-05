#!/usr/bin/python3
"""hbthn_hedare module have one function that fetch request-id of the header"""
import urllib.request
import sys


def main():
    """fetch request-id of the header for a giving url"""
    url = sys.argv[1:][0]
    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.getheader('X-Request-Id')
            print(request_id)
    except urllib.error.URLError as e:
        pass


if __name__ == '__main__':
    main()
