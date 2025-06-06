#!/usr/bin/python3

"""Importe le module 'json' pour pouvoir décoder une chaîne JSON"""
import json

"""Convertit une chaîne JSON en objet Python."""""
def from_json_string(my_str):

    """
    Utilise json.loads pour décoder la chaîne JSON
    Retourne l objet Python obtenu (liste, dict, etc.)
    """
    return json.loads(my_str)
