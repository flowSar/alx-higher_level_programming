#!/usr/bin/node

const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
