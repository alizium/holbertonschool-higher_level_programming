#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Trouver les éléments qui sont dans un seul set mais pas les deux"""
    od_set = set_1 ^ set_2
    return od_set
