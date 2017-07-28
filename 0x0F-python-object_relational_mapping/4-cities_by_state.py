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
        "SELECT cities.id, cities.name, states.name FROM cities"
        " INNER JOIN states ON cities.state_id = states.id ORDER"
        " BY cities.id ASC;")
    cities_rows = cur.fetchall()
    for city in cities_rows:
        print(city)
    cur.close()
    conn.close()
