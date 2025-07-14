#!/usr/bin/node

// prend tous les mots que la personne a tapés
const args = process.argv;

// garde seulement les mots que la personne a ajoutés (on retire les 2 premiers)
const nbArgs = args.length - 2;

// Si la personne n’a rien tapé après .js
if (nbArgs === 0) {
  console.log("No argument");  // Je dis "pas d’argument"
}
// Si elle a mis 1 seul mot
else if (nbArgs === 1) {
  console.log("Argument found");  // Je dis "argument trouvé"
}
// Sinon (elle a mis 2 mots ou plus)
else {
  console.log("Arguments found");  // Je dis "des arguments trouvés"
}
