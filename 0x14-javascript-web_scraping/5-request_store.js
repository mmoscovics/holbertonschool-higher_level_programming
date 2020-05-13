#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[1], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
