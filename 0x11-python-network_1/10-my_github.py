#!/usr/bin/python3
"""Takes Github credentials, uses Github API to display id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://api.github.com/user"
    try:
        r = requests.get(url, auth=(argv[1], argv[2])).json()
        print(r["id"])
    except:
        print("None")
