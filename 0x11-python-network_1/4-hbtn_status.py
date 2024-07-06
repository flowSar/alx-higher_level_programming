#!/usr/bin/python3
"""fetch URL request body"""
import requests


def main():
    """fetch URL request body"""
    url = 'https://alx-intranet.hbtn.io/status'
    re = requests.get(url)
    print('Body response:')
    print("\t- type: {}".format(type(re.text)))
    print("\t- content: {}".format(re.text))


if __name__ == '__main__':
    main()
