#!/usr/bin/python3


"""
Ce module contient une fonction qui vérifie si un objet hérite
(directement ou indirectement) d'une classe donnée,
sans être une instance directe de cette classe.
"""


def inherits_from(obj, a_class):

    """
    Vérifie si l'objet `obj` hérite (directement ou indirectement)
    de la classe `a_class`, sans être une instance directe de `a_class`.

    Args:
        obj: l'objet à tester
        a_class: la classe supposée "mère"

    Returns:
        True si obj hérite de a_class (mais n'est pas exactement a_class)
        False sinon
        """

    if isinstance(obj is a_class) and type(obj) is not a_class:
        return True
    else:
        return False
