#!/usr/bin/node

/* Prints square usinf # */
const arg = parseInt(process.argv[2]);

if (arg === parseInt(process.argv[2])) {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
