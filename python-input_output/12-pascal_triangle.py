#!/usr/bin/python3

"""genere un triangle de pascal"""


"""Retourne le triangle de Pascal jusqu'à la ligne n (comprise)."""
def pascal_triangle(n):

    """Si n est inférieur ou égal à 0, retourne une liste vide"""
    if n <= 0:
        return []

    """Initialise le triangle avec la première ligne contenant [1]"""
    triangle = [[1]]

    """Construit chaque ligne du triangle à partir de la précédente"""
    for i in range(1, n):
        row = [1]
        prev = triangle[i - 1]

        """Calcule les valeurs intermédiaires de la ligne"""
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])

        """Termine chaque ligne avec un 1"""
        row.append(1)
        """Ajoute la ligne au triangle"""
        triangle.append(row)

    return triangle
