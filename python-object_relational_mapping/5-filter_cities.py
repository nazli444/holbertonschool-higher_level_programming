#!/usr/bin/python3
"""Lists all cities of a given state (safe from SQL injection)"""
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
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
