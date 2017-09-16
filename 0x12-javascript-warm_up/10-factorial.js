#!/usr/bin/node
// script that computes and prints a factorial
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = Number(process.argv[2]);
console.log(factorial(num));
