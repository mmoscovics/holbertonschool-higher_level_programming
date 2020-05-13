#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + data.statusCode);
});
