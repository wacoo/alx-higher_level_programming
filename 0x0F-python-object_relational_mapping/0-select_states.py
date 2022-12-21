#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    db.query(""" SELECT * FROM states ORDER BY states.id ASC""")
    res = db.store_result()
    for r in res.fetch_row(maxrows=0):
        print(r)
