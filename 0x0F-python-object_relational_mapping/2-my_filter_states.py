#!/usr/bin/python3
''' List all the states in a table'''
import MySQLdb
import sys

if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB1 = sys.argv[3]

    database1 = MySQLdb.connect(host="localhost", user=USER, passwd=PASS, db=DB1, port=3306, charset="utf8")
    cur = database1.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for r in rows:
        if r[1] == argv[4]:
            print(r)

    cur.close()
    database1.close()
