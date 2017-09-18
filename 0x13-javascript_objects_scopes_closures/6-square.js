#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js
const firstSquare = require('./5-square').Square;

firstSquare.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.width));
  }
};

exports.Square = firstSquare;
