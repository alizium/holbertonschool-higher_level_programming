#!/usr/bin/python3
"""Affiche tout les objets de la base de donnée hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():

    """Liste des villes par nom"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ Connexion SQLAlchemy"""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    main()