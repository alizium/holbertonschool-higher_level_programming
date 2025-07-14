#!/usr/bin/node

// on prend tous les arguments à partir de l'index 2
const args = process.argv.slice(2).map(Number);

// Si moins de 2 arguments, on affiche 0
if (args.length < 2) {
  console.log(0);
} else {
  // on tri du plus grand au plus petit
  args.sort((a, b) => b - a);
  console.log(args[1]); // Deuxième plus grand
}
