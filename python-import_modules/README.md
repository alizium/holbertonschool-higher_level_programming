# Python - Modules, Importation et Arguments

Ce README résume les concepts essentiels de Python concernant les modules, l'importation de fonctions, et les arguments en ligne de commande, en s'appuyant sur la documentation officielle.

## 🔥 Pourquoi Python est génial
- Une syntaxe simple et lisible, proche du langage humain
- Puissant : utilisé pour le web, les jeux, la data, l’IA, l’automatisation, etc.
- Immense communauté et nombreuses bibliothèques
- Fonctionne sur tous les systèmes
- Structure modulaire qui permet de réutiliser le code facilement

## 📥 Comment importer des fonctions depuis un autre fichier
Supposons un fichier `add_0.py` contenant :
```python
def add(a, b):
    return a + b
```
Dans un autre fichier, on peut importer la fonction ainsi :
```python
from add_0 import add
```

## 🛠 Comment utiliser une fonction importée
Une fois importée, on utilise :
```python
a = 1
b = 2
print(add(a, b))
```

## 📦 Comment créer un module
Un module est un simple fichier `.py` contenant des fonctions réutilisables.
Exemple :
```python
# mon_module.py
def saluer(nom):
    print(f"Bonjour, {nom} !")
```
Puis dans un autre fichier :
```python
from mon_module import saluer
saluer("Jean Michel")
```

## 🔍 Comment utiliser la fonction intégrée dir()
`dir()` permet de voir les fonctions et attributs d’un objet ou module :
```python
import math
print(dir(math))
```

## 🚫 Comment empêcher l’exécution lors d’une importation
Encadre ton code avec :
```python
if __name__ == "__main__":
    # Ce code s'exécute uniquement si le fichier est lancé directement
    ma_fonction()
```

## 💻 Comment utiliser les arguments en ligne de commande
Utiliser le module `sys` :
```python
import sys
print(sys.argv)
```
- `sys.argv[0]` = nom du script
- `sys.argv[1]`, `sys.argv[2]`, etc. = les arguments passés

Exemple :
```bash
python3 script.py Jean
# Affiche : ['script.py', 'Jean']
```