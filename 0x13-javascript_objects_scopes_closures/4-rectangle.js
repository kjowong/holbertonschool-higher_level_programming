#!/usr/bin/node
// class Rectangle that defines a rectangle
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };
  this.double = function () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  };
  this.rotate = function () {
    [this.width, this.height] = [this.height, this.width];
  };
};
