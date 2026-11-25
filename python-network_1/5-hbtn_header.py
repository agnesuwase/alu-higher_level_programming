#!/usr/bin/python3
"""Takes in a URL and displays the X-Request-Id header of the response."""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
