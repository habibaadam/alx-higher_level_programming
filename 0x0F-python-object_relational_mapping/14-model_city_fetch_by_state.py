#!/usr/bin/python3
"""
a script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    creating a sql engine with username as first arg
    password as second arg
    and then the database as the third argument
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = Session(engine)
    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for C, x in cities:
        print("{}: ({}) {}".format(x.name, C.id, C.name))
    session.commit()
    session.close()
