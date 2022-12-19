#!/usr/bin/node

/* Print two arguments by adding 'is' inside */
const noArgs = (process.argv.length) - 2;
const args = process.argv;

if (noArgs <= 0) {
  console.log('No argument');
} else {
  console.log(args[2] + ' is ' + args[3]);
}
