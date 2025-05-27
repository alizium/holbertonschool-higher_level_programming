#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

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


"""
Definis une classe enfant Rectangle qui herite de son parent BaseGeometry :

Cette classe représente un rectangle
défini par une largeur (width) et une hauteur (height).

Lorsqu on crée un rectangle, on doit donner deux nombres :
            - la largeur
            - la hauteur

        Ces deux nombres doivent être :
            - des entiers (pas du texte, pas des booléens etc.)
            - strictement supérieurs à zéro (0)

        Si ce n est pas le cas, le programme renvoie une erreur.

        Exemple d'utilisation :
        r = Rectangle(4, 6)

        Ce rectangle sera stocké en mémoire avec deux valeurs,
        invisibles de l extérieur :
            __width (la largeur)
            __height (la hauteur)

        Cette classe utilise une fonction héritée de la classe BaseGeometry
        pour vérifier automatiquement que les données sont correctes.
        """


class Rectangle(BaseGeometry):

    """Constructeur de la classe rectangle"""

    def __init__(self, width, height):

        """Instance integer_validator"""

        def integer_validator(self, name, value):

            """stock la largeur de la hauteur dans un attribut privé"""

            self.integer_validator("width", width)
            self.integer_validator("height", height)

            self.__width
            self.__height
