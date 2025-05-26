#!/usr/bin/python3

class MyClass1:

    def lookup(obj):

        """
        fonction lookup : prend un objet en paramètre
        et retourner la liste des attributs et des méthodes de cet objet
        """

        return dir(obj)
