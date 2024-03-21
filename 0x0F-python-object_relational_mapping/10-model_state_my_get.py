#!/usr/bin/python3
"""
Script to print the State object with the name passed as an argument from the database hbtn_0e_6_usa
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
    state_name = sys.argv[4]

    # Create an engine and a session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the state's id or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
