#!/usr/bin/python3
"""Takes in URL and email, sends POST Request to URL"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    data = parse.urlencode(email)
    with request.urlopen(argv[1], data.encode()) as response:
        print(response.read().decode("utf-8"))
