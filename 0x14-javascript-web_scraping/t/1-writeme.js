#!/usr/bin/node
/*
 * write data to file
 */

const fs = require('fs');
const arg = process.argv;

fs.writeFile(arg[2], arg[3], (err) => {
  if (err) {
    console.error(err);
  }
});
