#!/usr/bin/python3


"""DEFINIS CLASSE ETUDIANTE"""


class Student:

    """REPRESENTE L'IDENTITE DE L'ETUDIANT (age etc)."""

    def __init__(self, first_name, last_name, age):

        """INITIALISE UNE NOUVELLE INTANCE/ENTITE D'ETUDIANT"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """RETOURNE DICTIONNAIRE QUI REPRESENTE L'ETUDIANT"""
        return self.__dict__
