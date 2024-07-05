#!/usr/bin/python3
"""fetch URL by using urllib"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
    print(f"Body response:")
    print(f"  - type: {type(body)}")
    print(f"  - content: {body}")
    print(f"  - utf8 content: {body.decode('utf-8')}")
