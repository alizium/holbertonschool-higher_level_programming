#!/usr/bin/env python3

"""Verboselist herite de la classe list"""
class VerboseList(list):

    """declation de la methode append qui sert a ajouter"""
    def append(self, item):
        """
        super permet d'appeler la methode du parent de cette classe
        append ajoute l'item
        """
        super().append(item)
        print(f"Added {item} to the list.")

    """permet d'ajouter une iterable (liste)"""
    def extend(self, iterable):
        """on appelle la methode extend avec super et iterable comme arg"""
        super().extend(iterable)
        """affiche texte et nombre elements dans iterable"""
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        '''enleve item de la liste'''
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """enleve l'item de la liste"""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
