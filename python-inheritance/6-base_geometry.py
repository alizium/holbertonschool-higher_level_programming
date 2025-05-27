#!/usr/bin/python3


"""Definis une classe vide BaseGeometry"""


class BaseGeometry:

    """Definis une instance area"""

    def area(self):

        """Affiche message d'erreur personnalisé : area n'est pas implementé"""

        raise Exception("area() is not implemented")
