#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    """Creer un dictionnaire avec la valeur de l ancien * 2
    Sans modifier l'original"""

    # creation nouveau dictionnaire vide
    new_dict = {}
    # Pour cle dans dictionnaire (l'original)
    for key in a_dictionary:
        # Creer une nouvelle cle qui utilise l'original mais *2
        new_dict[key] = a_dictionary[key] * 2
    # Retourne le nouveau dictionnaire
    return new_dict
