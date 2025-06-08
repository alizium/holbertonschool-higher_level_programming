#!/usr/bin/python3

"""importe pickle"""

import pickle

"""CustomObject classe avec serialization et deserialization."""


class CustomObject:

    """definis un objet personnalisé avec :
    le nom l'age et le statut de l'etudiant"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):

        """affiche l'attribut de l'objet."""

        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):

        """
        Serialize l'objet courant à l'objet specifique
        Args:
            filename (str): Path to the output file.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            pass  # Silently fail as per instructions

    @classmethod
    def deserialize(cls, filename):

        """
        Deserialize un objet de son fichier
        """

        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
