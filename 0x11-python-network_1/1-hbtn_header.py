#!/usr/bin/python3
"""Takes in URL to fetch and display X-Request-Id"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(reponse.headers.get("X-Request-Id"))
