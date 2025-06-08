#!/usr/bin/python3

"""Lis un fichier CSV et converti en format JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):

    """
    Convertis données CSV en fichier JSON 'data.json'.

    affiche True si la conversion s'est bien déroulé, False si non
    """

    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
