#!/usr/bin/node
// function that executes x times a function
exports.callMeMoby = function (n, func) {
  for (let i = 0; i < n; i++) {
    func();
  }
};
