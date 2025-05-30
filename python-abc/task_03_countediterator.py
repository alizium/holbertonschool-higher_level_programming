#!/usr/bin/env python3

"""definis une classe CountedIterator"""


class CountedIterator:

    """definis le constructeur qui permettra d'utiliser un iterable"""
    def __init__(self, iterable):
        """stock l'iterateur"""
        self.iterator = iter(iterable)
        """commence a 0"""
        self.count = 0

    def get_count(self):
        """retourne la valeur du compteur"""
        return(self.count)

    def __next__(self):
        """incremente grace au compteur"""
        self.count += 1
        """retourne la valeur d'iterator"""
        return next(self.iterator)
