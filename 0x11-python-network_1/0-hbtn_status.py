#!/usr/bin/python3
"""Fetches url"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - conent: {}".format(html))
    print("    - utf8 content: {}".format(html.decode("utf-8")))
