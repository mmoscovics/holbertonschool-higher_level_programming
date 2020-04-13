#!/usr/bin/python3
"""Takes in URL, sends request to URL for error code"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    err = r.status_code
    if err >= 400:
        print("Error code: {}".format(err))
    else:
        print(r.text)
