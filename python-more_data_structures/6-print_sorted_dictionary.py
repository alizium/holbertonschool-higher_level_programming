#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Trie dans l'ordre alphabetique"""
    for key in sorted(a_dictionary.keys()):
        print("{}".format(a_dictionary[key]))
