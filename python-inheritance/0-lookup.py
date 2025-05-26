#!/usr/bin/python3

def lookup(obj):
    """
    Fonction lookup : prend un objet en paramètre
    et retourne la liste des attributs et des méthodes de cet objet.
    """
    return dir(obj)
