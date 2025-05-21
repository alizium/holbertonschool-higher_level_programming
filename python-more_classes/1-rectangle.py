#!/usr/bin/python3

"""Classe Rectangle qui accepte des dimensions (width et height)"""


class Rectangle:
    """Classe définit rectangle avec attributs privés width et height."""

    def __init__(self, width=0, height=0):
        """Initialise rectangle avec largeur et hauteur, avec vérification."""
        self.height = height
        self.width = width

        """
        @property : lis la valeur d'un attribut privé comme s'il était public
        exemple : print(rectangle.width)

        Getter: récupère la valeur d'un attribut privé.
        Setter: définis ou modifier la valeur d'un attribut privé.
        """

    @property
    def height(self):
        """Setter de la largeur avec vérification de type et de valeur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter de la hauteur avec vérification."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter de la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter de la largeur avec vérification."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
