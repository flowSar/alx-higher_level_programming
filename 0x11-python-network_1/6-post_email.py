#!/usr/bin/python3
"""send a post request """
import requests
import sys


def main():
    """send a POST request to the passed URL with the email as a parameter"""
    url = sys.argv[1:][0]
    email = sys.argv[1:][1]
    data = {'email': email}
    re = requests.post(url, data)
    print(f"{re.text}")


if __name__ == '__main__':
    main()
