#!/usr/bin/python3

"""
Ajoute du texte à la fin d un fichier texte (UTF-8)
et retourne le nombre de caractères ajoutés.
"""


def append_write(filename="", text=""):

    """
    Ouvre le fichier en mode ajout ("a") avec encodage UTF-8
    Crée le fichier s'il n'existe pas
    Ajoute le texte à la fin du fichier sans effacer ce qui est déjà dedans
    """
    with open(filename, "a", encoding="utf-8") as f:

        """
        Écrit le texte dans le fichier
        Stocke le nombre de caractères ajoutés dans la variable nb_chars
        """
        characters_written = f.write(text)

        """Retourne le nombre de caractères ajoutés"""
        return characters_written
