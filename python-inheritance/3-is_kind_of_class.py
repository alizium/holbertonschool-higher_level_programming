#!/usr/bin/python3


"""
Contient une fonction qui vérifie si un objet est une instance directe
ou héritée d'une classe donnée.
"""


def is_kind_of_class(obj, a_class):

    """
    Vérifie si un objet est une instance directe ou héritée d'une classe.

    Cette fonction retourne True si l'objet obj est une instance de a_class,
    ou si obj est une instance d'une classe qui hérite de a_class.

    Paramètres :
    obj -- l'objet à tester
    a_class -- la classe de référence

    Retourne :
    True si obj est une instance (ou héritier) de a_class, sinon False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
