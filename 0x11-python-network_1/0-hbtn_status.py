#!/usr/bin/python3
"""Fetches url with urllib"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- conent: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
