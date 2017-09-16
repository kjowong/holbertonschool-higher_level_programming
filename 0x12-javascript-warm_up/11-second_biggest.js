#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
let intArr = process.argv.splice(2);
function sortArr (a, b) {
  return a - b;
}
intArr.sort(sortArr);
if (intArr.length < 2) {
  console.log('0');
} else {
  console.log(intArr[intArr.length - 2]);
}
