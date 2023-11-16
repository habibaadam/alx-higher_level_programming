#!/usr/bin/python3
"""A script that lists states from a database where names start with N"""
import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for h in states:
        if h[1][0] == 'N':
            print(h)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
