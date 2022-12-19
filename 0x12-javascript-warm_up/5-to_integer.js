#!/usr/bin/node

/* Converts first agument to integer and prints */
const args = process.argv;
const arg = parseInt(args[2]);

if (arg === parseInt(args[2])) {
  console.log('My number:', arg);
} else {
  console.log('Not a number');
}
