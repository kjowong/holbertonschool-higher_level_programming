#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = list.filter(toSearch => toSearch === searchElement).length;
  return count;
};
