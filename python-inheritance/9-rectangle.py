#!/usr/bin/python3

"""
Definis une classe enfant Rectangle qui herite de son parent BaseGeometry :
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
