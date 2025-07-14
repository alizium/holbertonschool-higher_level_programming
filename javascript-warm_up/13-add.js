#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));  // Affiche 8

// on définis une fonction "add" qui additionne deux nombres
exports.add = function (a, b) {
  return a + b;
};
