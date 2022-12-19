#!/usr/bin/node

/* Prints Argument(s) found or Nor argument message depending on the number of arguments */

const noArgs = (process.argv.length) - 2;

if (noArgs <= 0) {
  console.log('No argument');
} else if (noArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
