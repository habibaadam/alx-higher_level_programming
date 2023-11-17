#!/usr/bin/python3
"""A script that lists all cities from a database"""
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
    query = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id=states.id"""
    cursor.execute(query)
    cities = cursor.fetchall()
    for h in cities:
        print(h)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
