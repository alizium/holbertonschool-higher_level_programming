#!/usr/bin/node

// Quand on clique sur l’élément avec l’ID toggle_header
document.querySelector("#toggle_header").addEventListener("click", function () {
  // On sélectionne la balise <header>
  const header = document.querySelector("header");

  // Si <header> a déjà la classe "red"
  if (header.classList.contains("red")) {
    // On enlève "red" et on met "green" à la place
    header.classList.remove("red");
    header.classList.add("green");
  } else {
    // Sinon, on enlève "green" et on met "red" à la place
    header.classList.remove("green");
    header.classList.add("red");
  }
});