#!/usr/bin/python3
"""
A python script that lists the 10 most recent commits from a repository
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    )

    q = requests.get(url)
    all_commits = q.json()
    try:
        for h in range(10):
            print("{}: {}".format(all_commits[h].get("sha"),
                  all_commits[h].get("commit").get("author").get("name")))
    except IndexError:
        pass
