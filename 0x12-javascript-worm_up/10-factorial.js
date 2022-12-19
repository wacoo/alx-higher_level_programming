#!/usr/bin/node

/* Computes and prints a factorial */
const args = process.argv;

function factorial (num) {
  if (num === 0) {
    return 1;
  } else if (isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(parseInt(args[2])));
