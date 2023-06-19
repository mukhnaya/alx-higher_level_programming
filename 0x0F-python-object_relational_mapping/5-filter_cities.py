#!/usr/bin/python3
'''a script that takes in the name of a state as an argument and lists all cities of that state'''
import MySQLdb
import sys

if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB1 = sys.argv[3]

    database1 = MySQLdb.connect(host="localhost", user=USER, passwd=PASS, db=DB1, port=3306, charset="utf8")
    cur = database1.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities INNER JOIN states on cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    my_list = []
    for r in rows:
        if r[1].searched:
            my_list.append(r[0])
    print1 = ", ".join(my_list)
    print(print1)

    cur.close()
    database1.close()
