#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Create an engine
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, passwd, db))
    # Create a custom session object class from the database engine
    Session = sessionmaker(bind=engine)

    # Create an instance of the new custom session class
    session = Session()

    # Fetch all City objects and display them by state
    results = session.query(State.name, City.id, City.name)\
        .join(City, City.state_id == State.id).order_by(City.id)

    for result in results:
        print("{}: ({}) {}".format(result[0], result[1], result[2]))

    # Close the session
    session.close()
