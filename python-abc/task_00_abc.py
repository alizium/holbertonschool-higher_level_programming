#!/usr/bin/env python3

"""import de ABC et abstractmethod"""

from abc import ABC, abstractmethod


"""
La classe Animal est une classe abstraite, c est-à-dire un modèle général pour d'autres classes.

Elle ne sert pas à créer des animaux directement, mais à dire ce que toutes les classes 
d'animaux devraient avoir. Par exemple, un chien ou un chat hériteront de cette classe.

Cette classe utilise le module 'abc' (Abstract Base Classes) pour définir une méthode 
abstraite appelée 'sound'. Une méthode abstraite est une méthode qui n a pas de contenu ici,
mais qui est OBLIGATOIRE dans les classes qui héritent de Animal.

En résumé :

- On ne peut pas créer un objet Animal directement (ce serait une erreur).
- Toute classe qui hérite de Animal DOIT avoir sa propre version de la méthode 'sound'.
- C est une manière de forcer les classe qui hérite à définir certains comportements.
"""

class Animal(ABC):

    """methode abstraite appelee 'sound'"""
    @abstractmethod
    def sound(self):
        # elle n'a pas encore de fonction
        pass

class Dog(Animal):
    """Dog herite de la classe abstraite 'Animal' """

    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Cat qui herite de la classe abstraite 'Animal' 
    toutes les classes heritant de animal 
    ont la capacite de produire un bruit (sound)
    """
    def sound(self):
        return "Meow"
