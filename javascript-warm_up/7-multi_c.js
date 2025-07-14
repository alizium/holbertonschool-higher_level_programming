#!/usr/bin/node

// on récupère le nombre de fois qu'on dois afficher la phrase
const times = parseInt(process.argv[2]);

// on ce n’est pas un vrai nombre ou il manque : message d’erreur
if (isNaN(times)) {
  console.log("Missing number of occurrences");
} else {
  // Sinon on fait une boucle pour afficher la phrase x fois
  for (let i = 0; i < times; i++) {
    console.log("C is fun");
  }
}
