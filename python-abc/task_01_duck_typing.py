#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""mehtode abstraite"""


class Shape(ABC):
    """Classe abstraite qui définit le modèle pour toute forme géométrique."""

    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme."""
        pass
