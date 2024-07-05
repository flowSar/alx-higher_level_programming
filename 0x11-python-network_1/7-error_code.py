#!/usr/bin/python3
"""status code """
import requests
import sys


def main():
    """print status code if it's >= 400"""
    url = sys.argv[1:][0]
    try:
        re = requests.get(url)
        if re.status_code == 200:
            print(re.text)
        elif re.status_code >= 400:
            print(f"Error code: {re.status_code}")
    except requests.RequestException as e:
        pass


if __name__ == '__main__':
    main()
