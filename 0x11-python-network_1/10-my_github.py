#!/usr/bin/python3
"""use Github API to get user ID"""
import requests
import sys


def main():
    """use Github API to get ID or a user that passed
    """
    username = sys.argv[1:][0]
    password = sys.argv[1:][1]
    url = 'https://api.github.com/octocat'
    headers = {
        'Authorization': f'Bearer {password}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    try:
        re = requests.get(url, headers=headers)
        if re.status_code == 200:
            user_data = re.json()
            print(f'{user_data['id']}')
    except Exception as e:
        pass


if __name__ == '__main__':
    main()
