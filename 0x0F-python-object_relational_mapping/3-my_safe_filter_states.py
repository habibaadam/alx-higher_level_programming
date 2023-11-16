#!/usr/bin/python3
"""A script that  write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT id, name FROM states where name = %s ORDER BY id ASC"

    cursor.execute(query, (sys.argv[4] + '%',))

    states = cursor.fetchall()
    for h in states:
        print(h)
