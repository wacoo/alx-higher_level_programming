#!/usr/bin/none

/* Returns number of ocurrences in the a list */

exports.nbOccurrences = function (list, searchElement) {
  let tmp = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      tmp++;
    }
  }
  return tmp;
};
