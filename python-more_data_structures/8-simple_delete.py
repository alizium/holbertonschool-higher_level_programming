#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Supprime dans le dictionnaire a_dictionary la clé nommée key"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
