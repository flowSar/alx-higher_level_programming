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
    try:
        re = requests.post(url, auth=HTTPBasicAuth(username, token))
        if re.status_code == 200:
            user_data = re.json()
            print(f'user_data{user_data['id']}')
    except Exception as e:
        pass


if __name__ == '__main__':
    main()
