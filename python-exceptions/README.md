🔹 try :
On utilise try pour dire à Python : "essaie ce bloc de code, mais s’il y a une erreur, ne plante pas"

    print(1 / 0)  # erreur : division par zéro


🔹 except :
Si une erreur survient dans le bloc try, on passe dans le bloc except, un texte d'erreur s'affichera alors. 

try:
    print(1 / 0)
except ZeroDivisionError:
    print("On ne peut pas diviser par zéro !")


🔹 else (optionnel)
Si aucune erreur ne survient dans le bloc try, alors le bloc else s’exécute.

try:
    print("Tout va bien")
except:
    print("Erreur !")
else:
    print("Pas d'erreur donc on passe ici")


🔹 finally (optionnel) :
Ce bloc est toujours exécuté, qu’il y ait une erreur ou non. On l’utilise souvent pour libérer des ressources (fichiers, connexions, etc.).

try:
    print("Essai")
except:
    print("Erreur !")
finally:
    print("Toujours exécuté")


🔹 raise :
Permet de déclencher volontairement une exception.

age = -1
if age < 0:
    raise ValueError("L'âge ne peut pas être négatif")



💡 Types courants d'exceptions :

ZeroDivisionError	Division par zéro
IndexError	Index hors de la liste
TypeError	Mauvais type d’opération (ex : "abc" + 5)
ValueError	Mauvaise valeur passée à une fonction
KeyError	Clé absente dans un dictionnaire
NameError	Variable non définie
FileNotFoundError	Fichier introuvable

📚 Exemple complet

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : division par zéro.")
        return None
    else:
        print("Division réussie !")
        return result
    finally:
        print("Opération terminée.")

print(safe_divide(10, 2))  # ➜ 5.0
print(safe_divide(10, 0))  # ➜ Erreur
