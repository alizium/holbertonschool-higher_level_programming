#!/usr/bin/python3

"""permet de lire le fichier filename"""

def read_file(filename=""):

    """Ouvrir le fichier en mode lecture ('r') avec l'encodage 'utf-8' en utilisant le with statement
    Donne un nom à ce fichier ouvert, comme f"""

    with open(filename, "r", encoding="utf-8") as f:

        # lis et retourne le contenu du fichier f.read
        print(f.read())
