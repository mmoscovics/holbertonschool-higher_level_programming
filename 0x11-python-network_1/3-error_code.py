#!/usr/bin/python3
"""Takes in URL, sends request to URL, manage HTTPError"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as httperr:
        print("Error code: {}".format(httperr.code))
