#!/usr/bin/node

// Sélectionne la balise avec l'ID "red_header" et attend qu'on clique dessus
document.querySelector("#red_header").addEventListener("click", function () {

	// Quand on clique, change la couleur du texte de la balise <header> en rouge
	document.querySelector("header").style.color = "#FF0000";
});
