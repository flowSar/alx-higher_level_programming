#!/usr/bin/python3
"""send a post request"""
import requests
import sys


def main():
    """send a POST request to the passed URL with the letter as a parameter
        and fetch json data
    """
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = ''
    else:
        letter = sys.argv[1:][0]
    try:
        data = {'q': letter}
        re = requests.post(url, json=data)
        json_data = re.json()

        if len(json_data) == 0:
            print('No result')
        elif not isinstance(json_data, dict):
            print('Not a valid JSON')
        else:
            print(f"[{json_data['id']}] {json_data['name']}")
    except requests.RequestException as e:
        pass


if __name__ == '__main__':
    main()
