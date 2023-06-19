#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
import sys

if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB1 = sys.argv[3]

    database1 = MySQLdb.connect(host="localhost", user=USER, passwd=PASS, db=DB1, port=3306, charset="utf8")
    cur = database1.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for r in rows:
        if r[1].startswith("N"):
            print(r)

    cur.close()
    database1.close()
