Héritage et Concepts Orientés Objet en Python
9.5 Héritage
L'héritage permet à une classe (classe dérivée) d'hériter des attributs et des méthodes d'une autre classe (classe de base). La syntaxe ressemble à ceci :
class DerivedClassName(BaseClassName):
<statements>
Concepts clés :
- Classe de Base : La classe dont on hérite.
- Classe Dérivée : La classe qui hérite d'une autre classe.
Si la classe de base se trouve dans un autre module, vous pouvez spécifier le chemin complet comme `module_name.BaseClassName`.

Comment fonctionne l'héritage :
1. Résolution des attributs : Lorsque vous demandez un attribut dans une classe dérivée, Python le recherche d'abord dans la classe dérivée. Si cet attribut n'est pas trouvé, il le recherche dans la classe de base. Ce processus continue de manière récursive si la classe de base est elle-même dérivée d'une autre classe.
2. Résolution des méthodes : Lorsqu'une méthode est appelée sur une instance de la classe dérivée, Python vérifie si la méthode existe dans la classe dérivée. Si elle n'existe pas, elle la recherche dans la classe de base, et ainsi de suite.

Méthodes de remplacement :
Une classe dérivée peut remplacer des méthodes de la classe de base. Si une méthode de la classe de base appelle une autre méthode de la même classe de base, et que cette méthode est remplacée dans la classe dérivée, la méthode de la classe dérivée sera appelée à la place.

Appeler des méthodes de la classe de base :
Vous pouvez appeler explicitement une méthode de la classe de base en utilisant `BaseClassName.methodname(self, arguments)`.

Fonctions liées à l'héritage :
Python propose deux fonctions intégrées liées à l'héritage :
- `isinstance()`: Vérifie si un objet est une instance d'une classe ou d'une sous-classe.
    isinstance(obj, int)  # Vrai si obj est une instance de int ou de ses sous-classes
- `issubclass()`: Vérifie si une classe est une sous-classe d'une autre classe.
    issubclass(bool, int)  # Vrai, car bool est une sous-classe de int

9.5.1 Héritage multiple
Python prend en charge l'héritage multiple, où une classe peut hériter de plusieurs classes de base. La syntaxe ressemble à ceci :
class DerivedClassName(Base1, Base2, Base3):
<statements>

Comment fonctionne l'héritage multiple :
1. Recherche des attributs : Lorsque vous recherchez un attribut, Python suit une recherche profondeur d'abord, de gauche à droite. Cela signifie qu'il recherchera l'attribut dans `DerivedClassName`, puis `Base1`, et ainsi de suite.
2. Ordre de résolution des méthodes (MRO) : Cet ordre change dynamiquement pour gérer les scénarios d'héritage multiple, en veillant à ce que chaque classe de base soit accédée une seule fois.

Exemple de MRO :
Si une classe hérite de plusieurs classes et qu'elles partagent certaines méthodes, Python utilise l'ordre de résolution des méthodes pour décider quelle méthode appeler.

9.6 Variables privées
Python n'a pas de véritables variables "privées" comme certaines autres langages. Cependant, il existe une convention :
- Une variable précédée d'un underscore (par exemple, `_spam`) est considérée comme "non publique" et ne doit pas être accédée directement à l'extérieur de la classe.

Mutilation de noms :
Pour éviter les conflits de noms dans les sous-classes, Python utilise la **mutilation de noms**. Si une variable commence par `__` (deux underscores au début), Python change le nom de la variable en `_classname__variable`. Cela permet d'éviter l'écrasement accidentel des variables privées dans les sous-classes.

Exemple de mutilation de noms :
```python
class Example:
    def __init__(self):
        self.__private = 42
```
9.7 Divers
Dataclasses :
Python propose les `dataclasses` pour regrouper facilement des données nommées.
```python
from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    dept: str
    salary: int
```
9.8 Itérateurs
Les itérateurs permettent de parcourir les éléments d'un conteneur (par exemple, des listes, des dictionnaires). La boucle `for` fonctionne avec des itérateurs en arrière-plan.
Vous pouvez créer des itérateurs personnalisés en définissant les méthodes `__iter__()` et `__next__()` dans une classe.

9.9 Générateurs
Les générateurs sont une manière compacte d'écrire des itérateurs. Au lieu d'utiliser `__iter__()` et `__next__()`, vous pouvez utiliser le mot-clé `yield` dans une fonction régulière.
Exemple de générateur :
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)
```
9.10 Expressions de générateurs
Une forme compacte de générateurs utilisant une syntaxe similaire aux compréhensions de listes, mais avec des parenthèses.
Exemple :
```python
sum(i*i for i in range(10))  # somme des carrés
```
Mots-clés et définitions
1. **Héritage** : Le mécanisme par lequel une classe peut acquérir les attributs et méthodes d'une autre classe.
2. **Classe de Base** : Une classe dont on hérite.
3. **Classe Dérivée** : Une classe qui hérite d'une autre classe.
4. **Ordre de Résolution des Méthodes (MRO)** : L'ordre dans lequel Python cherche des méthodes dans une hiérarchie de classes.
5. **Héritage Multiple** : Une fonctionnalité de Python où une classe peut hériter de plusieurs classes de base.
6. **Variables Privées** : Les variables destinées à être utilisées uniquement au sein de la classe, généralement indiquées par un underscore (`_`) ou par la mutilation de noms (`__`).
7. **Dataclasses** : Une fonctionnalité de Python permettant de créer facilement des classes qui contiennent des données, grâce au décorateur `@dataclass`.
8. **Itérateur** : Un objet permettant de parcourir les éléments d'un conteneur.
9. **Générateur** : Un type d'itérateur créé en utilisant le mot-clé `yield`.
10. **Expression de Générateur** : Une syntaxe compacte pour créer des générateurs, similaire aux compréhensions de listes.


Concepts d'Héritage en Python
Qu'est-ce qu'une superclasse, une classe de base ou une classe parente ?
Une superclasse (ou classe de base, ou classe parente) est une classe dont une autre classe hérite. Elle contient des attributs et des méthodes qui seront partagés avec les classes qui en hériteront.
Qu'est-ce qu'une sous-classe ?
Une sous-classe est une classe qui hérite d'une ou plusieurs superclasses (classes de base). Elle peut ajouter de nouveaux attributs et méthodes, ou bien remplacer (surcharger) ceux de la classe parente.
Comment lister tous les attributs et méthodes d'une classe ou d'une instance ?
Tu peux utiliser la fonction `dir()` pour lister tous les attributs et méthodes d'une classe ou d'une instance. Exemple :```pythondir(ma_classe) # Liste les attributs et méthodes de la classedir(ma_instance) # Liste les attributs et méthodes de l'instance```
Quand une instance peut-elle avoir de nouveaux attributs ?
Une instance peut avoir de nouveaux attributs lorsqu'ils sont ajoutés dynamiquement, c'est-à-dire après la création de l'objet, en accédant directement à l'instance. Par exemple :```pythonmon_objet.nouvel_attribut = 10```Cela fonctionne même si l'attribut n'existe pas dans la classe de base.
Comment hériter d'une classe ?
Pour hériter d'une classe en Python, tu utilises la syntaxe suivante :```pythonclass SousClasse(NomDeLaClasseParent): pass```Cela permet à la sous-classe d'hériter des méthodes et des attributs de la classe parente.
Comment définir une classe avec plusieurs classes de base ?
Tu peux définir une classe qui hérite de plusieurs classes de base en les spécifiant dans les parenthèses lors de la déclaration de la classe :```pythonclass MaClasse(SuperClasse1, SuperClasse2): pass```
Quelle est la classe par défaut de toutes les classes ?
La classe par défaut de toutes les classes en Python est `object`. Si tu ne spécifies pas de classe parente, ta classe héritera automatiquement de `object` :```pythonclass MaClasse: pass```Ici, `MaClasse` hérite de `object` implicitement.
Comment surcharger une méthode ou un attribut hérité de la classe parente ?
Pour surcharger une méthode ou un attribut d'une classe parente, tu définis une méthode avec le même nom dans la sous-classe. Par exemple :```pythonclass ClasseParent: def methode(self): print('Méthode de la classe parente')class SousClasse(ClasseParent): def methode(self): print('Méthode de la sous-classe')instance = SousClasse()instance.methode() # Cela affichera 'Méthode de la sous-classe'```
Quels attributs ou méthodes sont disponibles par héritage pour les sous-classes ?
Les sous-classes héritent de tous les attributs et méthodes publics de la classe parente. Si un attribut ou une méthode est privé (précédé de `__`), il sera manglé et ne pourra pas être directement accédé, sauf s'il utilise des méthodes spéciales pour y accéder.
Quel est le but de l'héritage ?
Le but de l'héritage est de favoriser la réutilisation du code. Il permet de créer une nouvelle classe (sous-classe) à partir d'une classe existante (superclasse), d'y ajouter des fonctionnalités spécifiques ou de modifier celles de la classe parente sans avoir à réécrire tout le code.
Quelles sont, quand et comment utiliser les fonctions intégrées `isinstance`, `issubclass`, `type` et `super` ?
- **`isinstance()`** : Cette fonction permet de vérifier si un objet est une instance d'une classe ou d'une sous-classe. ```python isinstance(obj, MaClasse) # Retourne True si obj est une instance de MaClasse ou de ses sous-classes. ```- **`issubclass()`** : Cette fonction permet de vérifier si une classe est une sous-classe d'une autre. ```python issubclass(SousClasse, ClasseParent) # Retourne True si SousClasse est une sous-classe de ClasseParent. ```- **`type()`** : Cette fonction renvoie le type (classe) d'un objet. Elle peut être utilisée pour vérifier la classe d'un objet. ```python type(obj) # Retourne la classe de l'objet obj. ```- **`super()`** : Cette fonction permet d'appeler une méthode de la classe parente depuis la sous-classe, en particulier lorsqu'on surcharge des méthodes. ```python super().methode() # Appelle la méthode de la classe parente. ```

