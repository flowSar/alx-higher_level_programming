#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0 || !this.height || !this.width) {
      delete this.width;
      delete this.height;
    }
  }
}

module.exports = Rectangle;
