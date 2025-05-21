# README : Projet Python - Classe Rectangle

Ce fichier README contient une explication de **tous les mots-clés**, **concepts** et **analogies** utilisés dans les exercices liés à la classe `Rectangle` en Python. Il est conçu pour aider à comprendre non seulement ce que signifient ces mots, mais aussi comment et pourquoi on les utilise.

---

## 🧠 MOTS-CLÉS & CONCEPTS EXPLIQUÉS

### 1. `class`

* **C'est quoi** : Une structure pour créer des objets (comme un moule).
* **Analogie** : C’est comme une recette. Une fois écrite, on peut faire plein de gâteaux (objets) à partir d’elle.

---

### 2. `__init__()`

* **C'est quoi** : Une méthode spéciale qui initialise l’objet quand il est créé.
* **Analogie** : C’est comme emménager dans une maison et la meubler dès le départ.

---

### 3. `self`

* **C'est quoi** : Représente l’objet actuel (comme "moi" dans l’objet).
* **Analogie** : Chaque objet dit "Je suis moi". C’est ça `self`.

---

### 4. `attribut privé`

* **C'est quoi** : Variable qui commence par `__`, accessible seulement à l’intérieur de la classe.
* **Analogie** : Comme un journal intime caché dans un tiroir. Toi seul peux l’ouvrir.

---

### 5. `@property`

* **C'est quoi** : Transforme une méthode en attribut accessible comme une variable.
* **Analogie** : Une porte automatique. Tu rentres sans avoir à tourner la clé.

### 6. `@nom.setter`

* **C'est quoi** : Permet de modifier un attribut de manière contrôlée.
* **Analogie** : Une serrure intelligente qui vérifie si tu mets bien la bonne chose dans la boîte.

---

### 7. `TypeError` et `ValueError`

* **C'est quoi** : Erreurs (exceptions) à attraper quand les données sont mauvaises.
* `TypeError` = type incorrect (ex : texte au lieu de nombre)
* `ValueError` = valeur logique incorrecte (ex : largeur -5)
* **Analogie** : Quelqu’un qui paie avec des billets Monopoly (TypeError) ou qui veut acheter un truc qui vaut -10€ (ValueError).

---

### 8. `area()`

* **C'est quoi** : Retourne l’aire (largeur × hauteur).
* **Analogie** : Comme calculer la surface pour acheter un tapis.

### 9. `perimeter()`

* **C'est quoi** : Retourne le périmètre (distance autour du rectangle).
* **Analogie** : Comme mesurer la longueur d’une clôture pour un jardin.

---

### 10. `__str__()`

* **C'est quoi** : Définit ce qu’on affiche quand on fait `print(objet)`.
* **Analogie** : C’est comme la façon dont quelqu’un se présente à voix haute.

### 11. `__repr__()`

* **C'est quoi** : Représentation "officielle" de l’objet, pour pouvoir le recréer.
* **Analogie** : Quelqu’un qui donne son nom et son identifiant complet pour qu’on puisse le retrouver.

### 12. `eval()`

* **C'est quoi** : Exécute une chaîne de texte comme si c’était du code Python.
* **Analogie** : Lire une recette écrite et cuisiner immédiatement ce qu’elle décrit.

---

### 13. `__del__()`

* **C'est quoi** : Méthode appelée quand l’objet est supprimé.
* **Analogie** : Quelqu’un qui dit au revoir en partant d’une fête.

---

### 14. `number_of_instances`

* **C'est quoi** : Variable de classe qui compte combien d’objets existent.
* **Analogie** : Compter combien de gâteaux tu as faits avec ta recette.

---

### 15. `attribut de classe vs attribut d’instance`

* **attribut de classe** : Partagé par tous les objets (comme le moule).
* **attribut d’instance** : Propre à chaque objet (comme le glaçage d’un seul gâteau).

---

### 16. `print_symbol`

* **C'est quoi** : Variable de classe qui définit le caractère utilisé pour dessiner le rectangle.
* **Analogie** : Choisir si tu veux dessiner avec des étoiles ou des hashtags.

---

### 17. `staticmethod`

* **C'est quoi** : Méthode qui ne dépend ni de l’objet ni de la classe.
* **Analogie** : Une fonction dans la maison qui ne regarde ni les habitants ni les plans.

---

### 18. `bigger_or_equal()`

* **C'est quoi** : Méthode statique qui compare deux rectangles par leur aire.
* **Analogie** : Comparer deux gâteaux pour voir lequel nourrit plus de monde.

---

### 19. `classmethod`

* **C'est quoi** : Méthode qui utilise `cls` pour modifier ou créer un objet.
* **Analogie** : Une recette spéciale qui permet de faire une variante du gâteau.

### 20. `Rectangle.square(size)`

* **C'est quoi** : Une méthode de classe pour créer un carré (largeur = hauteur).
* **Analogie** : Demander au chef de faire un gâteau parfaitement carré au lieu d’un rectangle.