#!/usr/bin/python3

"""Importe le module de base pour créer un serveur HTTP"""
import http.server
import socketserver  # gère la connexion reseau
import json  # module pour travailler avec le format de données JSON


"""class MyHandler va hériter d'une autre classe"""


class MyHandler(http.server.BaseHTTPRequestHandler):

    """
    Définit la fonction qui sera appelée chaque fois
    que le serveur reçoit une requête GET (quand on ouvre une URL)
    """
    def do_GET(self):

        """
        Si le chemin demandé est la racine
        (par exemple, http://localhost:8000/)
        """
        if self.path == '/':

            """Envoie le code de statut ok 200 au navigateur"""
            self.send_response(200)

            """Indique que le contenu envoyé est du texte brut
            et communique la taille exacte du message au navigateur
            """
            self.send_header("Content-type", "text/plain")

            """Marque la fin des en-têtes HTTP"""
            self.end_headers()

            """Envoie le message 'simple API'
            (converti en octets) au navigateur"""
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

            """Affiche le chemin de la requête dans le terminal du serveur"""
            print(self.path)

        elif self.path == '/data':  # Si le chemin demandé est '/data'

            """Crée un dictionnaire Python avec des données à envoyer"""
            mon_dictionnaire = {
                "name": "John",
                "age": 30,
                "city": "New York",
            }

            """Convertit le dictionnaire Python
            en une chaîne de caractères JSON"""
            json_string = json.dumps(mon_dictionnaire)

            """Envoie le code de statut 200 (OK)
            au navigateur pour la réponse JSON"""
            self.send_response(200)

            """Indique que le contenu envoyé est au format JSON.
            et communique la taille exacte de la chaîne JSON au navigateur"""
            self.send_header("Content-type", "application/json")

            """Marque la fin des en-têtes HTTP pour la réponse JSON"""
            self.end_headers()

            """Envoie la chaîne JSON (convertie en octets) au navigateur"""
            self.wfile.write(json_string.encode('utf-8'))

            """Affiche le chemin de la requête '/data' dans le terminal"""
            print(self.path)

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        # Si le chemin demandé n'est ni '/' ni '/data'.
        else:  # Pour gérer les chemins inconnus

            """Envoie le code de statut 404 (Non trouvé) au navigateur."""
            self.send_response(404)  # Not Found

            """Indique que la réponse d'erreur est du texte brut."""
            self.send_header("Content-type", "text/plain")

            error_message = "Endpoint not found"

            """Communique la taille du message d'erreur"""
            self.send_header("Content-Length", str(len(error_message.encode('utf-8'))))

            """Marque la fin des en-têtes pour la réponse 404"""
            self.end_headers()

            """Envoie le message d'erreur au navigateur"""
            self.wfile.write(error_message.encode('utf-8'))

            """Affiche un message d'erreur et le chemin inconnu dans le terminal"""
            print(f"Path not found: {self.path}")

"""Définit le numéro de port sur lequel le serveur écoutera les requêtes."""
NUMERO_PORT = 8000

"""Affiche le port choisi dans le terminal pour que tu saches où te connecter."""
print("Numero de port : {}".format(NUMERO_PORT))

"""Crée le serveur web, le lie à ton ordinateur ("localhost") et au port défini.
Il utilise MyHandler pour gérer les requêtes entrantes."""
with socketserver.TCPServer(("localhost", NUMERO_PORT), MyHandler) as httpd:

    """Lance le serveur indéfiniment. Il attendra et traitera les requêtes tant qu'il ne sera pas arrêté"""
    httpd.serve_forever()
