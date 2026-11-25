#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request and displays the body."""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
