#!/usr/bin/python3
"""List all states with a name starting with N
Your script should take 3 arguments:
mysql username, mysql password and database name
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    states = cur.fetchall()
    [print(state) for state in states]

    cur.close()
    db.close()