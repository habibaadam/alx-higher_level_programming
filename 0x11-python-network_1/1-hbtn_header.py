#!/usr/bin/python3
import urllib.request
import sys
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
"""
if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as reply:
        print(dict(reply.headers).get("X-Request-Id"))
