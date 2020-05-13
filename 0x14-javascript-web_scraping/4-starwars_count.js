#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  let count = 0;
  const results = body.results;
  for (const result of results) {
    const characters = result.characters;
    for (const character of characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
