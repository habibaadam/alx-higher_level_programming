#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """Creating the SQLAlchemy engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    """Creating a session """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Querying all State objects and corresponding City objects """
    query_result = session.query(State).all()

    """Displaying the results"""
    for state in query_result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    """Closing the session"""
    session.close()
