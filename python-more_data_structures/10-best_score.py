#!/usr/bin/python3

def best_score(a_dictionary):

    """retourne un dictionnaire,
    retourne la cle qui a la plus grande valeur
    si a_dictionary est vide, retourne none"""

    # Si a_dictionary est vide
    if not a_dictionary:
        # Retourne None
        return None

    # On fait une boucle pour trouver la plus grande valeur
    for key, value in a_dictionary.items():

        # On cree 2 variables
        max_value = 0
        max_key = None

        if value > max_value:
            max_value = value
            max_key = key

    return max_key
