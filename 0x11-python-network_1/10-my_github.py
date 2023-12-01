#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    u_name = sys.argv[1]
    p_word = sys.argv[2]
    url = "https://api.github.com/user"

    q = requests.get(url, auth=HTTPBasicAuth(u_name, p_word))
    print(q.json().get("id"))
