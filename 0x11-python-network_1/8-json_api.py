#!/usr/bin/python3
"""Takes in a letter, sends POST request to URL"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        letter = {"q": ""}
    else:
        letter = {"q": argv[1]}
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", letter).json()
        if "id" not in r or "name" not in r:
            print("No result")
        else:
            print("[{}] {}".format(r["id"], r["name"]))
    except:
        print("Not a valid JSON")
