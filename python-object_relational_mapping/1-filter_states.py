#!/usr/bin/python3
"""Lists states with names starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1],
                         sys.argv[2], sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
