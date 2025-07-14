#!/usr/bin/node

// on prend tous les arguments tapés dans le terminal
const args = process.argv;

// on regarde s’il y a un argument après le nom du fichier
// (à l'index 2 car les 2 premiers éléments sont automatiques)
if (args[2]) {
  console.log(args[2]); // on affiche ce que la personne a tapé
} else {
  console.log("No argument"); // S’il n’y a rien, j’affiche ce message
}
