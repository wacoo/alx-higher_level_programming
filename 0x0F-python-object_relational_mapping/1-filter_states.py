#!/usr/bin/python3

""" Lists all the states that start with N from the database"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    db.query("""SELECT * FROM states WHERE name LIKE 'N%'
             ORDER BY states.id ASC""")
    res = db.store_result()
    for r in res.fetch_row(maxrows=0):
        print(r)
    db.close()
