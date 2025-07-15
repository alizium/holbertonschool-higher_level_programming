#!/usr/bin/node

// on attends que la page HTML soit entièrement chargée
document.addEventListener("DOMContentLoaded", function () {
  // on va chercher "bonjour" depuis l’API
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(response => response.json()) // Je transforme la réponse en objet JS
    .then(data => {
      // on sélectionne l’élément avec l’ID hello
      const helloDiv = document.querySelector("#hello");

      // on met le mot "Bonjour" dedans
      helloDiv.textContent = data.hello;
    });
});
