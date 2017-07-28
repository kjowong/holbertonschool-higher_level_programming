#!/usr/bin/python3
""" script that prints first State object from the database hbtn_0e_6_usa """


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

Base = declarative_base()
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                    argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    search_state = argv[4]
    found = list()

    for state in session.query(State).filter(
            State.name.contains(search_state)).order_by(
            State.id).all():
        if state:
            found.append(state.id)
            print("{}".format(str(found[0])))
    if not found:
        print("Not found")
    session.close()
