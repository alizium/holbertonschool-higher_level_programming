#!/usr/bin/env python3

"""definis classe poisson"""


class Fish:

    """definis une fonction nager et l'habitat"""
    def swim(self):
        """cette fonction affiche un texte"""
        print("The fish is swimming")

    def habitat(self):
        """cette fonction affiche un texte"""
        print("The fish lives in water")


"""definis une fonction oiseau"""


class Bird:
    """definis une fonction voler et l'habitat"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


"""classe enfant qui herite des parents"""


class FlyingFish(Fish, Bird):
    """fonction nager"""

    def swim(self):
        print("The flying fish is swimming!")

    """fonction voler"""
    def fly(self):
        print("The flying fish is soaring!")
    """fonction habitat"""

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
