#!/usr/bin/node

// on récupère l’argument
const arg = process.argv[2];

// ol le convertis en nombre entier avec parseInt
const number = parseInt(arg);

// Si c’est pas un nombre, on affiche "Not a number"
if (isNaN(number)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${number}`);
}
