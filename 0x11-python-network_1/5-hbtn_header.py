#!/usr/bin/python3
"""fetch request id"""
import requests
import sys


def main():
    """fetch request id"""
    url = sys.argv[1:][0]
    try:
        re = requests.get(url)
        request_id = re.headers['X-Request-Id']
        if re.status_code == 200:
            print(f"{request_id}")
    except requests.RequestException as e:
        pass


if __name__ == '__main__':
    main()
