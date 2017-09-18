#!/usr/bin/node
// script that imports an array and computes a new array
const array = require('./100-data').list;
let newArray = array.map(function (n) {
  return n * array.indexOf(n);
});
console.log(array);
console.log(newArray);
