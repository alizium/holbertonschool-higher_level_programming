#!/usr/bin/python3
"""Classe Rectangle qui accepte des dimensions (width et height)"""

class Rectangle:
    """Classe définit rectangle avec attributs privés width et height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialise rectangle avec largeur et hauteur, avec vérification."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """message et décrémente le compteur lors de la suppression de l'instance."""
        Rectangle.number_of_instances -= 1
        print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

        """
        @property : lis la valeur d'un attribut privé comme s'il était public
        exemple : print(rectangle.width)

        Getter: lis la valeur d'un attribut privé.
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

    def area(self):
        """retourne l'aire du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """retourne le perimetre du rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        # multiplie par 2 pour retourner le perimetre
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation en string du rectangle avec #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Retourne une chaîne du rectangle comme un entier"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
