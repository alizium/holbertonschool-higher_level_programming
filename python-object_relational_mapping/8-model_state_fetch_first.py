#!/usr/bin/python3

"""Liste dans la base de données de tout les états contenant la lettre 'a' """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects to the database and lists states containing 'a'."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Connexion SQLAlchemy"""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    """Filtre tout les états contenant a"""

    states_with_a = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    """pour afficher"""

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()