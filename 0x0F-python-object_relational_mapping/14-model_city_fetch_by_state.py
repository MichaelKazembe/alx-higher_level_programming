#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
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

    # Set up the relationship between State and City
    State.cities = relationship('City', back_populates='state')
    # Create the database tables
    Base.metadata.create_all(engine)
    # Create a session
    session = sessionmaker(bind=engine)()

    # Query and print City objects
    result = session.query(City).order_by(City.id.asc()).all()
    for row in result:
        print('{}: ({}) {}'.format(row.state.name, row.id, row.name))

    # Close the session
    session.close()
