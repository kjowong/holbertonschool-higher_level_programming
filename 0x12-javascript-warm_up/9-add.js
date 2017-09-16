#!/usr/bin/node
// Script that prints the addition of  integers
(function add (a, b) {
  a = Number(process.argv[2]);
  b = Number(process.argv[3]);
  console.log(a + b);
})();
