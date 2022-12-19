#!/usr/bin/node

/* Find the second biggest integer in the list */
const args = process.argv;
let max = 0;
let sb = 0;
let tmp = 0;
if (args.length < 2) {
  sb = 0;
} else {
  for (let i = 2; i < args.length; i++) {
    tmp = parseInt(args[i]);
    if (tmp > max) {
      sb = max;
      max = tmp;
    } else {
      if (tmp > sb) {
        sb = tmp;
      }
    }
  }
}
console.log(sb);
