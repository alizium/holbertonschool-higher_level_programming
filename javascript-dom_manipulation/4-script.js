#!/usr/bin/node

// Quand on clique sur l'élément avec l'ID add_item...
document.querySelector("#add_item").addEventListener("click", function () {
	// on sélectionne la liste (ul) avec la classe my_list
	const list = document.querySelector(".my_list");

	// on crée un nouvel élément li
	const newItem = document.createElement("li");

	// on lui mets le texte "Item"
	newItem.textContent = "Item";

	// on ajoute le <li> dans la liste
	list.appendChild(newItem);
});
