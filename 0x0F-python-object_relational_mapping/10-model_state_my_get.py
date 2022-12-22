#!/usr/bin/python3

""" search state id given state name """

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy
from sys import argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4])
    is_empty = state.first() is None
    if is_empty:
        print("Not found")
    else:
        print(state[0].id)
