#!/usr/bin/python3

import json

"""Écrit un objet au format JSON."""


def save_to_json_file(my_obj, filename):

    """
    Ouvre le fichier en mode écriture ("w") avec encodage UTF-8
    Crée le fichier s'il n'existe pas
    Écrase le contenu s'il existe
    """

    with open(filename, "w", encoding="utf-8") as f:

        """
        Convertit l'objet en chaîne JSON avec json.dumps()
        Écrit cette chaîne dans le fichier
        """
        f.write(json.dumps(my_obj))
