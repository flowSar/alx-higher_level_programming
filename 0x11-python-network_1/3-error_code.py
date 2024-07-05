#!/usr/bin/python3
"""erro code module"""
import urllib.request
import sys


def main():
    """fetch url dsplay the body or the error code """
    url = sys.argv[1:][0]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    main()
