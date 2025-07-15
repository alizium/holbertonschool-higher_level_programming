#!/usr/bin/node

// Quand on clique sur l'élément avec l'ID red_header...
document.querySelector("#red_header").addEventListener("click", function () {
	// ...on ajoute la classe 'red' à la balise <header>, ce qui la rend rouge
	document.querySelector("header").classList.add("red")
});
