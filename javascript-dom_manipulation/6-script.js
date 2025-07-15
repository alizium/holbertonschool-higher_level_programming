#!/usr/bin/node

// on va chercher les infos sur le personnage 5 (Leia Organa)
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then(response => response.json()) // on transforme la réponse en objet JS
  .then(data => {
    // on sélectionne l'élément avec l'ID character
    const character = document.querySelector("#character");

    // on affiche le nom du personnage dedans
    character.textContent = data.name;
  });
