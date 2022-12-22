#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

""" Create A State object that creates state table """


str1 = 'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
engine = create_engine(str1)
Base = declarative_base()


class State(Base):
    """ A class that describes the american states """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))

    def __init__(self, name):
        """ inits the State object"""
        #self.id = uuid.uuid4()
        self.name = name


Base.metadata.create_all(engine)
