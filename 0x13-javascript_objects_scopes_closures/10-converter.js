#!/usr/bin/node

/* COnvert a number fro mbase 10 to another */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
