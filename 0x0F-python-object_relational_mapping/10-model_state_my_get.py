#!/usr/bin/python3
"""Lists first State objects from a database"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).filter(State.name == argv[4]).first()
    if first_state:
        print(first_state.id)
    else:
        print("Not found")
