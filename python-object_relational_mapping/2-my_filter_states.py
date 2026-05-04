#!/usr/bin/python3
"""Lists states filtered by user input"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        "localhost",
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(sys.argv[4])
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
