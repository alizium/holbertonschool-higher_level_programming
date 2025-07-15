#!/usr/bin/node

// on cherche tous les films Star Wars
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json()) // on transforme la réponse en objet JS
  .then(data => {
    // on sélectionne l'ul avec l'ID list_movies
    const list = document.querySelector("#list_movies");

    // on parcours tous les films dans les résultats
    data.results.forEach(movie => {
      // on crée un nouvel <li> pour chaque film
      const item = document.createElement("li");

      // on mets le titre du film dedans
      item.textContent = movie.title;

      // on l'ajoute à la liste
      list.appendChild(item);
    });
  });
