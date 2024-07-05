#!/usr/bin/python3
""""""
import urllib.request
import sys



def main():
    """"""
    url = sys.argv[1:][0]
    #try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
    #except urllib.error.HTTPError as e:
        #pass
        

if __name__ == '__main__':
    main()
