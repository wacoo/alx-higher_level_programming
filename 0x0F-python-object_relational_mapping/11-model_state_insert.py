#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

""" insert State object Luosiana to the database"""
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/()'.format(argv[1], argv[2], argv[3]))

Session = sessionmaker(bind=engine)
session = Session()

"""Insert a state"""

name = "Luosiana"
idd = 6
st = State(name)
session.add(st)
session.commit()

""" Show states """
ids = session.query(State.id).last()
print(ids[0])
