#!/usr/bin/python3

""" Accepts state name and displays data """

from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    c = db.cursor()
    q = 'SELECT * FROM states WHERE name = {} ORDER BY states.id ASC'.format(argv[4])
    c.execute(q)
    res = c.fetchall()
    for r in res:
        print(r)
    c.close()
    db.close()
