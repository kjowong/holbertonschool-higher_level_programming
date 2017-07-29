#!/usr/bin/python3
""" script that list all State objects from the database hbtn_0e_6_usa """


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2],
                                                    argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).all():
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
