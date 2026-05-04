#!/usr/bin/python3
"""Lists states matching user input (case-sensitive)"""
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
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
    cur.execute(query.format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
