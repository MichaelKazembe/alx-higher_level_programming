#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Create an engine
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, passwd, db))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all City objects and display them by state
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State)\
            .filter(State.id == city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()
