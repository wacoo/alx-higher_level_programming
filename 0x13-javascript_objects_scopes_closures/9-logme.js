#!/usr/bin/node

/* Prints number of arguments already printed and current argument */
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
