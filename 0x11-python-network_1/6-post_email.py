#!/usr/bin/python3
"""Takes URL and email, sends POST request to URL"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    r = requests.post(argv[1], email)
    print(r.text)
