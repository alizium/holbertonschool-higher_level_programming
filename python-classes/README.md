Comprendre en profondeur la POO avec Python : classes, objets, méthodes, attributs, encapsulation, etc.

📌 Mots-clés à connaître :
class, object, instance, self, __init__, attribute, method, @classmethod, @staticmethod, encapsulation, abstraction, inheritance, polymorphism, public, private, protected

───────────────────────────────────────────────

1. 📦 Qu’est-ce qu’un objet ?
Un objet est une entité qui contient à la fois :
- des **données** (attributs)
- et des **fonctions** (méthodes)

🔸 Exemple :
    une voiture = objet
    attributs : couleur, marque
    méthodes : démarrer(), freiner()

En Python, tout est objet :
    x = 42               # objet de type int
    s = "hello"          # objet de type str
    def f(): pass        # objet de type function
    import math          # math est un module (objet)

───────────────────────────────────────────────

2. 🧱 Créer une classe
Une **classe** est un modèle à partir duquel on crée des objets.

🔸 Exemple :

class Person:
    pass  # bloc vide

p = Person()  # création d'un objet (instance)

print(type(p))  # <class '__main__.Person'>

───────────────────────────────────────────────

3. 🧬 Attributs et Méthodes

🔸 Attribut = variable qui appartient à l'objet
🔸 Méthode = fonction qui appartient à l'objet

⚠️ Les méthodes prennent toujours `self` en premier paramètre, qui représente l’objet lui-même.

🔸 Exemple :

class Person:
    def say_hi(self):
        print("Hello!")

p = Person()
p.say_hi()  # Hello!

───────────────────────────────────────────────

4. 🚪 La méthode __init__

__init__ est un **constructeur** : il est appelé automatiquement quand tu crées un objet.

🔸 Exemple :

class Person:
    def __init__(self, name):
        self.name = name  # on crée un attribut d'instance

    def greet(self):
        print("Hi, I'm", self.name)

p = Person("Alice")
p.greet()  # Hi, I'm Alice

───────────────────────────────────────────────

5. 🎭 Encapsulation, Abstraction et Masquage

- **Encapsulation** : cacher l’intérieur de l’objet pour éviter les erreurs.
- **Abstraction** : montrer uniquement ce qui est utile.
- **Masquage** (Information hiding) : interdire/modérer l’accès direct à certaines données.

🔸 Conventions :
    public      → var
    protégé     → _var (usage interne recommandé)
    privé       → __var (nom "manglé", difficile d’accès)

🔸 Exemple :

class Robot:
    def __init__(self, name):
        self.name = name
        self._serial = "12345"        # protégé
        self.__password = "secret"    # privé

r = Robot("R2-D2")
print(r.name)        # OK
print(r._serial)     # Possible mais déconseillé
# print(r.__password) → Erreur

───────────────────────────────────────────────

6. 🧰 Méthodes de classe et statiques

- `@classmethod` : agit sur la classe (reçoit `cls`)
- `@staticmethod` : méthode indépendante

🔸 Exemple :

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    @classmethod
    def how_many(cls):
        print("Robots:", cls.population)

    @staticmethod
    def info():
        print("Je suis un robot !")

Robot.info()
Robot.how_many()

───────────────────────────────────────────────

7. 🧠 Variables de classe vs d’instance

- **Variable d’instance** : spécifique à chaque objet → `self.attribut`
- **Variable de classe** : commune à tous les objets → `Class.attribut`

🔸 Exemple :

class Animal:
    species = "Mammal"  # variable de classe

    def __init__(self, name):
        self.name = name  # variable d’instance

a1 = Animal("Chien")
a2 = Animal("Chat")

print(a1.species)  # Mammal
print(a2.name)     # Chat

───────────────────────────────────────────────

8. 📚 Résumé final

✅ class : mot-clé pour créer une classe
✅ object : instance d'une classe
✅ self : référence à l'objet courant
✅ __init__ : constructeur
✅ Attribut : variable associée à une classe ou un objet
✅ Méthode : fonction associée à une classe
✅ @classmethod : méthode liée à la classe
✅ @staticmethod : méthode indépendante
✅ _var : protégé
✅ __var : privé (nom mangling)
