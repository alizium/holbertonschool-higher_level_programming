#!/usr/bin/node

// on récupère la taille du carré
const size = parseInt(process.argv[2]);

// Si ce n’est pas un vrai nombre : message d’erreur
if (isNaN(size)) {
  console.log("Missing size");
} else {
  // Boucle pour chaque ligne
  for (let i = 0; i < size; i++) {
    // on affiche une ligne composée de "X" répété "size" fois
    console.log("X".repeat(size));
  }
}
