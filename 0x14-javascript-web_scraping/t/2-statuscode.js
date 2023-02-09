#!/usr/bin/node

/*
 * display the status code of a request
 */
const arg = process.argv;
const request = require('request');

request(arg[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${response.statusCode}`);
});
