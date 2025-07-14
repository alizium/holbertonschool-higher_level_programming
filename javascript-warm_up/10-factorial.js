#!/usr/bin/node

// on récupère le nombre donné
const n = parseInt(process.argv[2]);

// on fait une fonction récursive pour calculer le factoriel
function factorial(x) {
  if (isNaN(x) || x === 0) {
    return 1; // Par convention, factoriel de NaN ou 0 = 1
  }
  return x * factorial(x - 1); // Appel de la fonction elle-même
}

// on affiche le résultat
console.log(factorial(n));
