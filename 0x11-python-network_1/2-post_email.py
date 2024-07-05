#!/usr/bin/python3
"""POST requestusing urllib"""
import urllib.request
import sys


def main():
    """POST reuest to the giving url with email as parameter"""
    url = sys.argv[1:][0]
    email = sys.argv[1:][1]
    data = {'email': email}
    try:
        encoded_data = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, encoded_data)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(f"Your email is: {body}")

    except urllib.error.HTTPError as e:
        pass


if __name__ == '__main__':
    main()
