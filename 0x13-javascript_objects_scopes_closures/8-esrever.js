#!/usr/bin/node

/* returns the reversed version of a list */

exports.esrever = function (list) {
  const rlist = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    rlist[j] = list[i];
    j++;
  }
  return rlist;
};
