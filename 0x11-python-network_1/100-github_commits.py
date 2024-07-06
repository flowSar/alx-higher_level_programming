#!/usr/bin/python3
"""POST requestusing urllib"""
import requests
import sys


def main():
    """use Github API to get fetch commits owner and sha"""
    repo = sys.argv[1:][0]
    owner = sys.argv[1:][1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    re = requests.get(url)
    data = re.json()
    i = 0
    for json_data in data:
        if i < 10:
            try:
                author_name = json_data['commit']['author']['name']
                print(f"{json_data.get('sha')}: {author_name}")
                i += 1
            except KeyError:
                pass


if __name__ == '__main__':
    main()
