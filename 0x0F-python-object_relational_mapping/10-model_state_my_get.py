#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if len(sys.argv) == 5:
        state_name = sys.argv[4]
        instance = session.query(State).filter(State.name == state_name).first()
        if instance is None:
            print("Not found")
        else:
            print("{}".format(instance.id))
    else:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))

    session.close()
