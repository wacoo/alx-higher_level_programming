#!/usr/bin/node

/*
 * print starwars movie titles given episode number from api
 */
const request = require('request');
const arg = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${arg[2]}`;
request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
