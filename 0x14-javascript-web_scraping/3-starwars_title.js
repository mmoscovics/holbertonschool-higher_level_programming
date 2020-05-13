#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0];
request.get(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  console.log(body.title);
});
