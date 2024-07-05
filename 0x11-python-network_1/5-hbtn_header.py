#!/usr/bin/python3
"""fetch request id"""
import requests
import sys


def main():
    """fetch request id"""
    url = sys.argv[1:][0]
    re = requests.get(url)
    request_id = re.headers['X-Request-Id']
    print(request_id)


if __name__ == '__main__':
    main()
