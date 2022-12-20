#!/usr/bin/node

/* Creates a class Square that inherits from Rectangle */

const Rectangle = require('./5-square');

class Square extends Rectangle {
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
