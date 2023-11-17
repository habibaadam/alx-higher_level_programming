#!/usr/bin/python3
"""
a script that updates a State object into the database hbtn_0e_6_usa
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
    update_state = session.query(State).filter_by(id=2).first()
    update_state.name = "New Mexico"
    session.commit()
    session.close
