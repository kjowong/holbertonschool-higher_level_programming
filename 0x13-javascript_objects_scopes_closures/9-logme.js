#!/usr/bin/node
// function that prints the number of argument already printed and the new argument value

let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
