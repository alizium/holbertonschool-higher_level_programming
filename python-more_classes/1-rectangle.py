#!/usr/bin/python3

"""Classe Rectangle qui accepte des dimensions (width et height)"""


class Rectangle:
    """Classe définit rectangle avec attributs privés width et height."""

    def __init__(self, width=2, height=4):
        """Initialise un rectangle avec une largeur et une hauteur."""
        self.__width = width
        self.__height = width

        """
        @property : lis la valeur d'un attribut privé comme s'il était public
        exemple : print(rectangle.width)

        Getter: récupère la valeur d'un attribut privé.
        Setter: définis ou modifier la valeur d'un attribut privé.
        """

    # Ce qui vient après n'est pas une vraie variable, mais une fonction
    @property
    def width(self):
        """Getter de la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Setter de la largeur avec vérification de type et de valeur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter de la hauteur du rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
