#!/usr/bin/python3
"""Takes URL and email, sends POST request to URL"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {"email": argv[2]}
    r = requets.post(argv[1], data=email)
    print(r.text)
