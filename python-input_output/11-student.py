#!/usr/bin/python3


"""DEFINIS LA CLASSE STUDENT AVEC ATTRIBUTS MODIFIABLE"""


class Student:

    """REPRESENTE L'IDENTITE DE L'ETUDIANT (age etc)."""

    def __init__(self, first_name, last_name, age):

        """INITIALISE UNE NOUVELLE INTANCE/ENTITE D'ETUDIANT"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """..."""

        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):

        """CHANGE ATTRIBUT DU DICTIONNAIRE"""

        for key in json:
            setattr(self, key, json[key])
