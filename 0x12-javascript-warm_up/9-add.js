#!/usr/bin/node

/* A function that adds two arguments */

const args = process.argv;

function add (arg1, arg2) {
  console.log(arg1 + arg2);
}
add(parseInt(args[2]), parseInt(args[3]));
