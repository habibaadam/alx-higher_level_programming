#!/usr/bin/python3
"""A script that lists states from a database"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    passw = sys.argv[2]
    data_b = sys.argv[3]

    database = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=passw, database=data_b
    )
    cursor = database.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    states = cursor.fetchall()

    for state in states:
        print(state)
