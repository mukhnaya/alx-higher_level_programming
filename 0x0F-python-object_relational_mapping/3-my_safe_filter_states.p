#!/usr/bin/python3
''' a script that takes in an argument and displays all values'''
import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB1 = sys.argv[3]

    database1 = MySQLdb.connect(host="localhost", user=USER, passwd=PASS, db=DB1, port=3306, charset="utf8")
    cur = database1.cursor()
    cur.execute("SELECT * FROM states ORDER BY state.id")
    rows = cur.fetchall()
    for r in rows:
        if r[1] == argv[4]:
            print(r)

    cur.close()
    database1.close()
