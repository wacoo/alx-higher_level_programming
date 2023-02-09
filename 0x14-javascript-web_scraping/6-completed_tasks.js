#!/usr/bin/node
/*
 * given user id, show the number of completed tasks (API)
 */

const request = require('request');
const arg = process.argv;

request(arg[2], function (err, res, tbd) {
  if (err) {
    console.error(err);
  }
  if (res.statusCode === 200) {
    const completed = {};
    const tks = JSON.parse(tbd);
    for (let i = 0; i < tks.length; i++) {
      if (tks[i].completed === true) {
        if (completed[tks[i].userId] === undefined) {
          completed[tks[i].userId] = 1;
        } else {
          completed[tks[i].userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Error');
  }
});
