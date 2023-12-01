#!/usr/bin/python3
"""
Fetching https://alx-intranet.hbtn.io/status with requests package
"""
import requests

if __name__ == "__main__":
    q = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(q.text)))
    print("\t- content: {}".format(q.text))
