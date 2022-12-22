#!/usr/bin/python3

""" list all cities form database """
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.name, states.name FROM cities INNER JOIN  states
              WHERE cities.state_id = states.id ORDER BY cities.id ASC""")
    res = c.fetchall()
    for r in res:
        print(r)
    db.close
