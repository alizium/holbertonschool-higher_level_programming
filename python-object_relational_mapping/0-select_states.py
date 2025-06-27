#!/usr/bin/python3

"""Liste hbtn_0e_0_usa."""

import MySQLdb
import sys


def main():

    """Connection à la database"""
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Connexion à la base MySQL"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """Création et exécution de la requête (curseur)"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    """Affiche les résultats"""
    for row in rows:
        print(row)

    """fermeture"""
    cur.close()
    db.close()


if __name__ == "__main__":
    main()