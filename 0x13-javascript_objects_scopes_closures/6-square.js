#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.width; y++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
