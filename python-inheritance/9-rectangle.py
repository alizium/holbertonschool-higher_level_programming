#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
Definis une classe enfant Rectangle qui herite de son parent BaseGeometry :

Cette classe représente un rectangle
défini par une largeur (width) et une hauteur (height).

Lorsqu on crée un rectangle, on doit donner deux nombres :
    la largeur
    la hauteur

Ces deux nombres doivent être :
    des entiers (pas du texte, pas des booléens etc.)
    strictement supérieurs à zéro (0)

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

        """stock la largeur de la hauteur dans un attribut privé"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):

        """Multiplie largeur avec hauteur"""
        return self.__width * self.__height

    def __str__(self):
        """retourne les resultats en chaine de charactere"""
        return f"[Rectangle] {self.__width}/{self.__height}"
