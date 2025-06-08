#!/usr/bin/python3

"""SAUVEGARDER JSON."""

import json


def serialize_and_save_to_file(data, filename):

    """
    Convertis un dictionnaire Python en fichier JSON

    - Ecrase le fichier s'il existe déjà
    - Sauvegarde en utilisant l'encodage utf-8
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    charge un fichier JSON et retourne le contenu en tant que dictionnaire Python
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
