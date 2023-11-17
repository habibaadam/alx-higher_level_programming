#!/usr/bin/python3
"""
  a script that takes in the name of a state
  as an argument and lists all cities of that state,
  using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name FROM cities JOIN \
            states ON cities.state_id = states.id WHERE \
            states.name = %s ORDER BY cities.id ASC",
                   (argv[4],))

    cities = cursor.fetchall()
    if cities is not None:
        print(", ".join([h[1] for h in cities]))
    cursor.close()
    db.close()
