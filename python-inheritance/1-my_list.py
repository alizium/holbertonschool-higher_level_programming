#!/usr/bin/python3


"""
Contient une classe MyList qui hérite de la classe list.
Elle ajoute une méthode spéciale appelée print_sorted, 
qui permet d afficher la liste triée (sans la modifier).
"""

class MyList(list):
    """
    Classe MyList : une version personnalisée de la classe list.

    Hérite de la classe list, donc on peut l’utiliser comme une liste normale.
    Exemple : on peut faire my_list.append(3), my_list[0], etc.

    Elle ajoute une méthode :
    - print_sorted() : affiche les éléments de la liste, triés par ordre croissant.
    """

    def print_sorted(self):
        """
        Affiche la liste triée par ordre croissant (du plus petit au plus grand),
        mais sans changer l’ordre des éléments dans la liste originale.
        """
        print(sorted(self))
        return sorted(self)
