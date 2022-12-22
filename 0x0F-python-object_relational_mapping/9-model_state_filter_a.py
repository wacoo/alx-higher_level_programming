#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

""" list states with names the char a in them """
if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id.asc())
    for r in res:
        print(str(r.id) + ": " + r.name)
    session.close()
