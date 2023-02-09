#!/usr/bin/node
/*
 * get content of a page and store in a file
 */
const fs = require('fs');
const arg = process.argv;
const request = require('request');

request(arg[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(arg[3], body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
