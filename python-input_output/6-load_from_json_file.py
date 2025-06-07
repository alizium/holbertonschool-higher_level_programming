#!/usr/bin/python3

"""import de json"""

import json

"""Lit un fichier JSON et retourne l'objet correspondant"""


def load_from_json_file(filename):

    """Ouvre le fichier en lecture ("r") avec encodage UTF-8"""
    with open(filename, "r", encoding="utf-8") as f:

        """Lit tout le contenu du fichier sous forme de chaîne"""
        lire_fichier = f.read()
        """Convertit la chaîne JSON en objet Python et le retourne"""
        return json.loads(lire_fichier)
