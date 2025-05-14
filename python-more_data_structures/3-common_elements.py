#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Reçoit 2 ensembles (set_1 et set_2)
    Et renvoie un ensemble
    qui contient uniquement les éléments qu ils ont en commun
    """
    resultat = set_1 & set_2
    return resultat
