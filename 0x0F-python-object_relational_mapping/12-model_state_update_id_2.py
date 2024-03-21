#!/usr/bin/python3
"""
Script to change the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine and a session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    if state:
        state.name = "New Mexico"

    # Commit the changes and close the session
    session.commit()
    session.close()
