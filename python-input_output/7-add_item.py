#!/usr/bin/python3

"""importe les arguments"""
import sys

"""importe les fonctons :
-save to json
-load from json file
des fichier 5 et 6"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Ignore le premier argument en utilisant une tranche"""
args = sys.argv[1:]

try:
    """ Tente de charger la liste depuis add_item.json """
    ma_liste = load_from_json_file("add_item.json")
except:
    """ Si le fichier n'existe pas ou est invalide, on démarre avec une liste vide"""
    ma_liste = []

"""étend la liste/ajoute des arguments"""
ma_liste.extend(args)

"""ajoute"""
save_to_json_file(ma_liste, "add_item.json")
