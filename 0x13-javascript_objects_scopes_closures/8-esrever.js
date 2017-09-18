#!/usr/bin/node
// function that returns the reserved version of a list
exports.esrever = function (list) {
  let reverseArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseArray.push(list[i]);
  }
  return reverseArray;
};
