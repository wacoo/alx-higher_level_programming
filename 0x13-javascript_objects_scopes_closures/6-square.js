#!/usr/bin/node

/* Creates a class Square that inherits from Rectangle */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) {
          process.stdout.write(c);
        } else {
          process.stdout.write('X');
        }
      }
      console.log('');
    }
  }
}

module.exports = Square;
