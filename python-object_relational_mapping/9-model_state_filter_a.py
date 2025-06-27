#!/usr/bin/python3


"""liste tout les objets contenant a."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connection à la database pour les 'a'"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """connexion à alchemy"""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
