#!/usr/bin/python3

"""
bibliothèque Python envoie des requêtes HTTP
bibliotheque python manipule fichiers csv
"""

import requests
import csv

def fetch_and_print_posts():
    """
    get : méthode HTTP qui demande des données à un serveur
    requests.get(url) : 
    Envoie requête get à une adresse URL (ex: un site ou une API)
    reponse : l'objet reçu en retour
    """


    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    """Accéder aux données renvoyées par l API
    et les transformer en objet Python (liste de dictionnaires)"""

    data = response.json()

    """affiche le titre dans le dictionnaire"""

    for post in data:
        print(post["title"])

def fetch_and_save_posts():
    """
    transforme données selectionnées en post.csv
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            posts = response.json()
            data = [
                {
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                } for post in posts
            ]

            with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
                writer.writeheader()
                writer.writerows(data)

        except (ValueError, KeyError):
            """ignore les erreurs"""
            pass
