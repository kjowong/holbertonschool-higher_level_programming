#!/usr/bin/node
// script that imports an array and computes a new array
const array = require('./100-data').list;
let newArray = array.map((num, index) => {
  return num * index;
});
console.log(array);
console.log(newArray);
