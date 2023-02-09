#!/usr/bin/node
/*
 * count the number of movies in which Wedge Antilles is present for API.
 */
const request = require('request');
const arg = process.argv;
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';

request(arg[2], function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const resl = JSON.parse(body).results;
  let count = 0;

  for (let i = 0; i < resl.length; i++) {
    const chara = resl[i].characters;
    if (chara.indexOf(actor) !== -1) {
      count++;
    }
  }
  console.log(count);
});
