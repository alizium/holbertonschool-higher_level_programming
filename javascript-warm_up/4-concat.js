#!/usr/bin/node

// on récupère les deux arguments que la personne a tapé
const args = process.argv;
const first = args[2];
const second = args[3];

// on crée une phrase "xxx is yyy" même si c’est undefined
console.log(`${first} is ${second}`);
