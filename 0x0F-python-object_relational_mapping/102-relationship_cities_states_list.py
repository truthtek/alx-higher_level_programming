#!/usr/bin/python3
"""
Script to list all City objects and corresponding State objects
from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
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

    # Query City objects and their corresponding State objects
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
