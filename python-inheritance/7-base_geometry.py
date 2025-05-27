#!/usr/bin/python3


"""Definis une classe vide BaseGeometry"""


class BaseGeometry:

    """Definis une instance area"""

    def area(self):

        """Affiche message d'erreur personnalisé : area n'est pas implementé"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que `value` est un entier strictement positif.

        Args:
        name (str): Le nom du paramètre (ex: "width", "age").
        value (int): La valeur à valider.

        Raises:
        TypeError: Si `value` n'est pas un entier.
        ValueError: Si `value` est inférieur ou égal à 0.

        Méthode utilisée pour valider des attributs dans d'autres classes.
        Elle affiche un message personnalisé en utilisant `name`.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
