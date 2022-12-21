#!/usr/bin/python3

""" Accepts state name and displays data safely"""

from sys import argv
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                     passwd=argv[2], db=argv[3])
c = db.cursor()
c.execute("""SELECT * FROM states WHERE name = %(name)s
          ORDER BY states.id ASC""", {'name': argv[4]})
res = c.fetchall()
for r in res:
    print(r)
db.close()
