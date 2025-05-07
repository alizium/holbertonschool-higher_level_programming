# conditions, boucles, fonctions...

## 📌 Pourquoi l’indentation est-elle si importante en Python ?

En Python, l’indentation (les espaces en début de ligne) **sert à organiser le code**.  
Elle permet de définir ce qui est à l’intérieur d’un bloc (comme un `if`, une boucle, une fonction…).  
⚠️ Si on oublie d’indenter ou qu'on met trop ou pas assez d’espaces, le programme renverra une erreur.

```python
# Correct
if True:
    print("Ceci est dans le if")

print("Ceci est en dehors du if")
```

## ✅ Comment utiliser les instructions `if`, `if ... else`, et `elif`

### `if`
```python
age = 18
if age >= 18:
    print("Tu es majeur")
```

### `if ... else`
```python
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

### `elif` (abréviation de "else if")
```python
note = 70

if note >= 90:
    print("Très bien")
elif note >= 70:
    print("Bien")
else:
    print("À améliorer")
```

## 💬 Comment utiliser les commentaires

Les commentaires servent à **expliquer le code**.  
Ils ne sont **pas exécutés** par le programme.

```python
# Ceci est un commentaire
age = 20  # On définit l'âge
```

## 🎯 Comment affecter des valeurs à des variables

On utilise `=` pour stocker une valeur dans une variable.

```python
nom = "Alice"
âge = 25
```

## 🔁 Comment utiliser les boucles `while` et `for`

### `while` (tant que)
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### `for` (pour chaque élément)
```python
for i in range(5):
    print(i)
```

## ⛔ Comment utiliser `break` et `continue`

- `break` **arrête la boucle**.
- `continue` **passe à l’itération suivante** sans exécuter le reste du bloc.

```python
for i in range(10):
    if i == 5:
        break  # On arrête tout
    if i == 3:
        continue  # On saute le 3
    print(i)
```


## ➕ Comment utiliser `else` avec les boucles

Tu peux ajouter un `else` **après une boucle**. Il s’exécute **seulement si la boucle se termine sans `break`**.

```python
for i in range(5):
    print(i)
else:
    print("Boucle terminée sans interruption")
```

## 🧘‍♀️ À quoi sert `pass` ?

`pass` signifie “ne rien faire”. On l’utilise quand Python attend un bloc de code, mais qu’on ne veut rien mettre pour le moment.

```python
def ma_fonction():
    pass  # Code à venir plus tard
```

## 🔢 Comment utiliser `range`

`range(n)` génère une suite de nombres de `0` à `n - 1`.

```python
for i in range(3):
    print(i)  # Affiche 0, 1, 2
```

## 🧩 Qu’est-ce qu’une fonction et comment l’utiliser ?

Une fonction est un bloc de code qu’on peut **réutiliser**.

```python
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
```

Avec paramètres :

```python
def saluer(nom):
    print("Bonjour", nom)

saluer("Marie")
```

## 🪣 Que retourne une fonction sans `return` ?

Si une fonction **n’utilise pas `return`**, elle retourne automatiquement **`None`** (c’est comme “rien”).

```python
def vide():
    print("Salut")

x = vide()
print(x)  # Affiche None
```

## 📦 Qu’est-ce que le scope des variables ?

Le **scope** (portée) définit **où une variable est accessible**.

- Variable dans une fonction → accessible **seulement dans la fonction**.
- Variable hors fonction → accessible **partout** dans le fichier.

```python
def test():
    x = 5  # locale
    print(x)

test()
# print(x)  # Erreur ! x n’existe pas ici
```

## 🐛 Qu’est-ce qu’un traceback ?

Un **traceback** est le message d’erreur affiché par Python.  
Il te dit **où l’erreur s’est produite** et **quel type d’erreur**.

Exemple :
```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero
```

## ➕ Quels sont les opérateurs arithmétiques ?

| Symbole | Nom                   | Exemple     | Résultat |
|---------|------------------------|-------------|----------|
| `+`     | addition               | `2 + 3`     | `5`      |
| `-`     | soustraction           | `5 - 2`     | `3`      |
| `*`     | multiplication         | `2 * 3`     | `6`      |
| `/`     | division               | `6 / 2`     | `3.0`    |
| `//`    | division entière       | `7 // 2`    | `3`      |
| `%`     | modulo (reste)         | `7 % 2`     | `1`      |
| `**`    | puissance              | `2 ** 3`    | `8`      |