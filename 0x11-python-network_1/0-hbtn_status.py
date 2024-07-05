#!/usr/bin/python3
"""fetch URL by using urllib"""
import urllib.request


def main():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        result = """Body response:\n\t- type: {}
        - content: {}\n\t- utf8 content: {}"""\
        .format(type(body), body, body.decode('utf-8'))
        print(result)


if __name__ == '__main__':
    main()
