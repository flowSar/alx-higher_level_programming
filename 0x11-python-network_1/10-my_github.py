#!/usr/bin/python3
"""use Github API to get user ID"""
import requests
import sys


def main():
    """use Github API to get ID or a user that passed
    """
    username = sys.argv[1:][0]
    password = sys.argv[1:][1]
    url = 'https://api.github.com/user'
    re = requests.get(url, auth=(username, password))
    json_data = re.json()
    if json_data == 0:
        print('None')
    else:
        print("{}".format(json_data['id']))


if __name__ == '__main__':
    """execute"""
    main()
