#!/usr/bin/python3

""" list cities by state"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT DISTINCT cities.name FROM cities, states WHERE
              cities.state_id = (SELECT id FROM states WHERE states.name =
              %s)""", (argv[4],))
    res = c.fetchall()
    lst = list(res)
    st = ', '.join([x[0] for x in lst])
    print(st)
    c.close()
    db.close()
