#!/usr/bin/node
/*
 * open and read file
 */

const fs = require('fs');
const arg = process.argv;

fs.readFile(arg[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
