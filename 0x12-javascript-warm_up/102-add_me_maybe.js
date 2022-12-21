#!/usr/bin/node

/* increment number and call function */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
