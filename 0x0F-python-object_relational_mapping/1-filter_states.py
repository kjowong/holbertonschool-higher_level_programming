#!/usr/bin/python3


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ code to be executed when imported """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    state_rows = cur.fetchall()
    for state in state_rows:
        print(state)
    cur.close()
    conn.close()
