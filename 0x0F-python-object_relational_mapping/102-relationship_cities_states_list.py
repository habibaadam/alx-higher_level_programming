#!/usr/bin/python3
"""
Script that lists all City objects
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

    """ Querying all corresponding City objects """
    query_result = session.query(City).all()

    """Displaying the results"""
    for city in query_result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
