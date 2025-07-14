#!/usr/bin/node

// on récupère les deux arguments
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// Je définis une fonction qui additionne deux nombres
function add(x, y) {
  return x + y;
}

// on affiche le résultat
console.log(add(a, b));
