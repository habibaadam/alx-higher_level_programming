#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
With the requests package
"""
import sys
import requests

if __name__ == "__main__":
    q = requests.get(sys.argv[1])
    print(q.headers.get("X-Request-Id"))
