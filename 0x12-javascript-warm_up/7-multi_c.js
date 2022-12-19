#!/usr/bin/node

/* Prints C is fun x times */
const arg = parseInt(process.argv[2]);

if (arg === parseInt(process.argv[2])) {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
