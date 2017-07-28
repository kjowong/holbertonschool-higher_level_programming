#!/usr/bin/python3


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from model_state import Base, State

Base = declarative_base()
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root",
                                                    "hbtn_0e_6_usa"))
    session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
