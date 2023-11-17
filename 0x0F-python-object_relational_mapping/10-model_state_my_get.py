#!/usr/bin/python3
"""
a script that lists State object with the name
passed as an argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

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
    name_arg = sys.argv[4]
    matching = session.query(State).filter_by(name=name_arg).first()
    if matching is not None:
        print(str(matching.id))
    else:
        print("Not found")
    session.close
