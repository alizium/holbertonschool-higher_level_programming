SQL = Structured Query Language
C’est un langage qui sert à manipuler des bases de données relationnelles.

Une base de données relationnelle est comme un classeur avec des tables. Chaque table ressemble à un tableur Excel avec des lignes (enregistrements) et des colonnes (champs).

MySQL est un logiciel de gestion de bases de données relationnelles, qui utilise le langage SQL.

On peut créer, lister, modifier, supprimer des bases de données et des tables.

On communique avec lui grâce à des commandes SQL.


Quand on execute :

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

Cela veut dire :

On montre le contenu du fichier 0-list_databases.sql (cat)...

et on le passes à MySQL (| mysql ...) pour qu’il l’exécute.

On se connectes au serveur MySQL sur notre propre ordinateur (-hlocalhost) avec l’utilisateur root (-uroot).

Il demande le mot de passe ensuite (-p).


Quelle commande SQL permet de lister les bases de données ?

SHOW DATABASES;
