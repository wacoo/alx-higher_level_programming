#!/usr/bin/node
/*
 * show all characters in a give movie in the right order (API).
 */
const request = require('request');
const arg = process.argv;
const film = `https://swapi-api.alx-tools.com/api/films/${arg[2]}`;

request(film, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  const chars = JSON.parse(body).characters;

  for (const cha in chars) {
    request(chars[cha], function (err2, res2, act) {
      if (err2) {
        console.error(err2);
      }
      console.log(JSON.parse(act).name);
    });
  }
});
