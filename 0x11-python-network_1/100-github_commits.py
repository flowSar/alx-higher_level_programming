#!/usr/bin/python3
"""POST requestusing urllib"""
import requests
import sys

def main():
    """use Github API to get fetch commits owner and sha
    """
    owner = sys.argv[1:][0]
    repo = sys.argv[1:][1]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    re = requests.get(url)
    data = re.json()
    for json_data in data:
        author_name = json_data['commit']['author']['name']
        print(f"{json_data['sha']} {author_name}")

if __name__ == '__main__':
    main()
