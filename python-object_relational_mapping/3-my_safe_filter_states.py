#!/usr/bin/python3
"""Safe filter states (SQL injection protected)"""
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
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
