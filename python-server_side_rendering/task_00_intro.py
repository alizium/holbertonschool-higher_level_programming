#!/usr/bin/python3

"""Création d'une fonction qui permet de générer des invitations personnalisées."""

# Définition de la fonction principale avec deux paramètres :
# - template : un texte modèle avec des {mots_clés}
# - attendees : une liste de dictionnaires contenant les données à insérer
def generate_invitations(template, attendees):

    # Vérifie que 'template' est bien une chaîne de caractères (du texte)
    if not isinstance(template, str):
        print("Erreur : le template doit être une chaîne de caractères.")
        return  # Si ce n'est pas le cas, on quitte la fonction

    # Vérifie que 'attendees' est bien une liste
    if not isinstance(attendees, list):
        print("Erreur : attendees doit être une liste de dictionnaires.")
        return  # Sinon on quitte la fonction

    # Parcourt la liste des invités pour vérifier que chaque élément est un dictionnaire
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Erreur : l'élément à l'index {i} n'est pas un dictionnaire.")
            return  # Si un élément n'est pas un dictionnaire, on quitte

    # Vérifie que le texte du modèle n'est pas vide (même après avoir enlevé les espaces)
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return  # On arrête si le modèle est vide

    # Vérifie que la liste d'attendees n'est pas vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return  # On arrête s’il n’y a aucun invité

    # Pour chaque invité, on va créer un fichier personnalisé
    for idx, attendee in enumerate(attendees, start=1):
        # On commence par copier le modèle de base
        invitation = template

        # Liste des mots à chercher et remplacer dans le modèle
        champs = ["name", "event_title", "event_date", "event_location"]

        # Pour chaque champ (mot clé entre accolades)
        for champ in champs:
            # On essaie de récupérer la valeur correspondante dans le dictionnaire
            valeur = attendee.get(champ)
            # Si la valeur est absente (None), on remplace par "N/A"
            if valeur is None:
                valeur = "N/A"
            # On remplace {champ} par la vraie valeur (ou "N/A") dans le texte
            invitation = invitation.replace("{" + champ + "}", str(valeur))

        # On essaie d’écrire l’invitation personnalisée dans un fichier texte
        try:
            # Le nom du fichier est output_1.txt, output_2.txt, etc.
            with open(f"output_{idx}.txt", "w") as f:
                f.write(invitation)  # On écrit l’invitation dans le fichier
        except Exception as e:
            # Si une erreur se produit (ex : pas de droit d'écriture), on l’affiche
            print(f"Erreur lors de l'écriture du fichier output_{idx}.txt : {e}")
