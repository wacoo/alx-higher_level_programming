#!/usr/bin/node

/* Prints the first argument passed to it */

const noArgs = (process.argv.length) - 2;
const args = process.argv;
if (noArgs <= 0) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
