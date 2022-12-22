#!/usr/bin/python3

""" Print the first row of the State object from database"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    is_empty = session.query(State).first() is None
    if not is_empty:
        first = session.query(State).first()
        print(str(first.id) + ": " + first.name)
    else:
        print("Nothing")
    session.close()
