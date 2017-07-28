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
    state_name = argv[4]
    cur = conn.cursor()
    cur.execute(
        "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities"
        " WHERE state_id IN (SELECT states.id from states WHERE"
        " name = '{}')".format(state_name))
    cities_rows = cur.fetchall()
    for city in cities_rows:
        print(city)
    cur.close()
    conn.close()
