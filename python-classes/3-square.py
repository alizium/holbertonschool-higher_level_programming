#!/usr/bin/python3


"""
Retourne l'aire (surface)
Contient la classe Square avec la verification de la taille.
"""
"""Classe qui définit un carré"""


class Square:

    """__size : taille du carré (doit être un entier >= 0)"""
    def __init__(self, size=0):

        """"Verifie si size est de type int"""
        if not isinstance(size, int):

            # Apparait un message d'erreur
            raise TypeError("Size must be an integer")

        """Verifie si size n'est pas negatif"""
        # Si size est plus petit que 0
        if size < 0:
            # Alors apparaitra un message d'erreur (value)
            raise ValueError("size must be >=")

        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: l aire (size * size)
        """
        return self.__size * self.__size
