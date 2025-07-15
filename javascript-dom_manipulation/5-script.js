#!/usr/bin/node

// Quand on clique sur l'élément avec l'ID update_header
document.querySelector("#update_header").addEventListener("click", function () {
  // on sélectionne la balise <header>
  const header = document.querySelector("header");

  // on remplace son texte par "New Header!!!"
  header.textContent = "New Header!!!";
});
