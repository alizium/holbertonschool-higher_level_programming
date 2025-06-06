#!/usr/bin/python3

"""
Importe le module standard 'json' pour convertir des objets Python en JSON
"""
import json


"""Retourne la représentation JSON d un objet Python sous forme de chaîne."""


def to_json_string(my_obj):

    """Utilise json.dumps pour convertir l objet en chaîne JSON
    Retourne cette chaîne"""
    return json.dumps(my_obj)
