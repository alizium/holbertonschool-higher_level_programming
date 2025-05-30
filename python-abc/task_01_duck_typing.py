#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

"""Classe abstraite qui herite d'ABC"""


class Shape(ABC):

    """définit le modèle pour toute forme géométrique."""

    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme."""
        pass


"""classe Circle qui herite de Shape"""


class Circle(Shape):

    """le constructeur prend radius en parametre"""
    def __init__(self, radius):
        """
        on affecte self.radius à radius pour dire a python
        que c'est la meme chose
        """
        self.radius = radius

    def area(self):
        """calcule et retourne l'aire du cercle"""
        return math.pi(self.radius**2)

    def perimeter(self):
        """calcule le perimetre du cercle"""
        return 2 * math.pi * self.radius


"""classe Rectangle qui herite de Shape"""


class Rectangle(Shape):

    """constructeur avec parametre largeur et hauteur"""
    def __init__(self, width, height):

        """on affecte self.width/self.height a width et height"""
        self.width = width
        self.height = height

    """methode area"""
    def area(self):

        """elle retourne largeur x hauteur"""
        return self.width * self.height

    """methode perimetre"""
    def perimeter(self):

        """Calcule et retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)


"""
fonction en dehors des classes :

elle prend un objet (ex : area ou perimeter) et elle affiche sa valeur
"""


def shape_info(shape):
    """on fait appel a area dans la classe shape pour obtenir sa valeur"""
    print(shape.area())
    print(shape.perimeter())
