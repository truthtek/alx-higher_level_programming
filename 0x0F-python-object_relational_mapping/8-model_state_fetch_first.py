#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa
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
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the first State object or "Nothing" if the table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
