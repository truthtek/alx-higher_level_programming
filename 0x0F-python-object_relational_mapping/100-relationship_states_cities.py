#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Create the State and City objects
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Add the objects to the session and commit
    session.add(state)
    session.add(city)
    session.commit()

    # Close the session
    session.close()
