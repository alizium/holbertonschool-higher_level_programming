#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Variable pour compter nb d'elements
    count_variable = 0

    # Boucle qui va tenter d'afficher les x premiers éléments
    # On tente d'afficher l'élément à l'index i de la liste
    for i in range(x):

        # try tente une action qui pourrait provoquer une erreur
        try:
            # On tente d'afficher l'element de l'index
            # Avec end="", on fait pas de retour à la ligne
            print(my_list[i], end="")
            # Si tout se passe bien, on augmente le compteur
            count_variable += 1
        # IndexError se produit quand on dépasse la taille d'une liste
        except IndexError:
            # "break" interrompt complètement la boucle en cours
            break
    # Après la boucle, on passe à la ligne suivante (affiche un saut de ligne)
    print()
    # La fonction renvoie le nombre réel d'éléments qui ont été affichés
    return count_variable
