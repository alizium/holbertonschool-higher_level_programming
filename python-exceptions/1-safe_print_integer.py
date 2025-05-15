#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Vérifie si value est un integer
        print("{:d}".format(value))
        # Retourne vrai si c'est le cas
        return True
    # Si ça ne l'est pas
    except (ValueError, TypeError):
        # Retourne faux
        return False
