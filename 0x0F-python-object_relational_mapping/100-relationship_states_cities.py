#!/usr/bin/python3
"""Creates State with City objects from a database"""
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    new_state.cities.append(new_city)
    session.add(new_state)
    session.add(new_city)
    session.commit()
