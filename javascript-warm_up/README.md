JavaScript est un langage qui permet de rendre les sites web vivants : cliquer, changer de couleur, faire apparaître/disparaître des choses…

🧠 Les mots-clés (tags) les plus utiles :


🟩 let :
Pour créer une variable qu’on peut changer plus tard.

let prénom = "Luna";
prénom = "Michel"; // ça marche


🟦 const :
Pour créer une variable qu’on ne peut plus changer.

const pays = "France";
pays = "Italie"; // ❌ Erreur !


🟥 var :
Ancienne façon de créer une variable. On ne l’utilise plus trop, car let et const sont plus clairs.


🔁 if, else :
Pour faire un choix.

let âge = 18;

if (âge >= 18) {
  console.log("Tu es majeur !");
} else {
  console.log("Tu es mineur !");
}


🔁 for :
Pour répéter une action plusieurs fois.

for (let i = 0; i < 3; i++) {
  console.log("Coucou !");
}


🧾 function
Pour créer une action qu’on peut réutiliser.

function direBonjour() {
  console.log("Bonjour !");
}

direBonjour(); // Appelle la fonction


👂 addEventListener :
Pour réagir à un clic (ou autre action).

document.getElementById("bouton").addEventListener("click", function() {
  alert("Tu as cliqué !");
});


🧱 Array (tableau) :
Pour garder plusieurs choses dans une seule variable.

let fruits = ["pomme", "banane", "fraise"];
console.log(fruits[1]); // "banane"


📘 String (chaîne de texte) :
Du texte entre guillemets.

let prénom = "Luna";


🔢 Number :
Un chiffre ou un nombre.

let âge = 25;
✅ Boolean
C’est vrai ou faux.

let estConnecté = true;
let aFini = false;


🧪 typeof :
Pour savoir le type d’une variable.

let âge = 30;
console.log(typeof âge); // "number"


📦 Object :
Un objet, c’est comme une boîte avec des étiquettes.

let personne = {
  nom: "Moore",
  âge: 25
};

console.log(personne.nom); // "Moore"
⚙️ Bonus : trucs utiles
🕳️ null et undefined
null = c’est vide exprès

undefined = c’est vide parce qu’on n’a rien mis


🧠 console.log() :
Pour afficher quelque chose dans la console (pour tester le code).

console.log("Hello, world !");


🧪 Exemple complet :

const prénom = "Luna";
let âge = 20;

if (âge >= 18) {
  console.log(prénom + " est majeure");
} else {
  console.log(prénom + " est mineure");
}