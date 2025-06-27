#!/usr/bin/python3

""" recherche database MySQL par nom """

import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """Connexion sur le serveur MySQL"""
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )


    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    query = query.format(state_name)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))


    cursor.close()
    db.close()