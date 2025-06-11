#!/usr/bin/python3

"""On importe la classe Flask depuis le module flask"""

from flask import Flask, jsonify, request

"""On crée une application Flask"""

app = Flask(__name__)

"""creation dictionnaire avec des utilisateurs"""
users = {}

"""Définit la route '/' qui renvoie un message de bienvenue"""
@app.route("/")
def home():
    """Retourne un message d'accueil"""
    return "Welcome to the Flask API!"

"""Définit la route '/status' pour vérifier que l'API fonctionne"""
@app.route("/status")
def status():
    """Retourne 'OK' si tout fonctionne"""
    return "OK"

"""Définit la route '/data' pour retourner la liste des utilisateurs"""
@app.route("/data")
def data():
    """Retourne tous les noms d'utilisateurs enregistrés"""
    return jsonify({"users": list(users.keys())})

"""Définit la route '/users/<username>' pour accéder à un utilisateur spécifique"""
@app.route("/users/<username>")
def get_user(username):
    """Si l'utilisateur existe, retourne ses informations"""
    if username in users:
        return jsonify(users[username])
    else:  # Sinon, retourne une erreur 404 avec un message
        return jsonify({"error": "User not found"}), 404

"""Définit la route '/add_user' pour ajouter un nouvel utilisateur via POST"""
@app.route('/add_user', methods=['POST'])
def add_user():
    """Récupère les données envoyées dans la requête POST"""
    data = request.get_json()
    """Vérifie si le champ 'username' est présent"""
    if "username" not in data:
        """Retourne une erreur 400 si 'username' est manquant"""
        return jsonify({"error": "Username is required"}), 400
    """Stocke le nom d'utilisateur depuis les données reçues"""
    username = data["username"]
    """Ajoute l'utilisateur au dictionnaire"""
    users[username] = data
    """Retourne une réponse avec code 201 et les données ajoutées"""
    return jsonify({"message": "User added", "user": data}), 201

"""Lance le serveur Flask si le fichier est exécuté directement"""
if __name__ == "__main__":
    """Démarre le serveur sur le port par défaut (5000)"""
    app.run()
