#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

""" insert State object Luosiana to the database"""
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    """Insert a state"""

    name = "Luosiana"
    st = State(name)
    session.add(st)
    session.flush()

    """ Show states """
    print(st.id)
    session.commit()
    session.close()

