#!/usr/bin/python3
"""
Script that lists all State objects that
contain the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Create an engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all State objects containing the letter 'a'
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
