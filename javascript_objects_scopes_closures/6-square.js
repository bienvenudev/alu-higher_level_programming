#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      c === undefined ? console.log('X'.repeat(this.size)) : console.log(c.repeat(this.width));
    }
  }
};
