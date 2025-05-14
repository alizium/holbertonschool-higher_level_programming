#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Enleve les doublons de la liste et retourne leur somme."""
    unique_values = set(my_list)
    return sum(unique_values)
