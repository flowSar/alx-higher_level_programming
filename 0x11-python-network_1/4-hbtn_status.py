#!/usr/bin/python3
""""""
import requests


def main():
    """"""
    url = 'https://alx-intranet.hbtn.io/status'
    re = requests.get(url)
    result = """Body response:\n\t- type: {}\n\t- content: {}"""\
        .format(type(re.text), re.text)
    print(result)


if __name__ == '__main__':
    main()
