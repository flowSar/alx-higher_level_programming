#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  size;
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
