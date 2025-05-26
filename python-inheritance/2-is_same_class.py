#!/usr/bin/python3

"""
    Vérifie si un objet est exactement une instance d'une classe donnée.
"""


def is_same_class(obj, a_class):

    """
    Cette fonction retourne True si l'objet obj est une instance directe
    de la classe a_class (pas une sous-classe). Sinon, elle retourne False.
    """
    """""
    Paramètres :
    obj -- l'objet à tester
    a_class -- la classe à comparer avec l'objet

    Retourne :
    True si obj est exactement une instance de a_class, False sinon.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
