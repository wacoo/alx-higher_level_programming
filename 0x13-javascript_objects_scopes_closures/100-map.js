#!/usr/bin/node

/* Script that imports an array and computes a new array */
const list = require('./100-data');
const nlist = list.list.map((x, y) => x * y);

console.log(list.list);
console.log(nlist);
