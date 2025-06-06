#!/usr/bin/python3

"""
Écrit du texte dans un fichier (UTF-8)
et retourne le nombre de caractères écrits.
"""


def write_file(filename="", text=""):

    """
    w ouvre le fichier en mode écriture avec encodage UTF-8
    Si le fichier n'existe pas, il sera créé
    Si le fichier existe, son contenu sera écrasé
    """
    with open(filename, "w", encoding="utf-8") as f:
        """
        Écrit le texte dans le fichier
        Stocke le nombre de caractères écrits dans la variable nb_chars
        """
        nb_chars = f.write(text)
        """retourne le nombre de caractère écrits"""
        return nb_chars
