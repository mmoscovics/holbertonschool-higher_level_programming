#!/usr/bin/python3
"""List State object and corresponding City objects in a database"""
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

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
