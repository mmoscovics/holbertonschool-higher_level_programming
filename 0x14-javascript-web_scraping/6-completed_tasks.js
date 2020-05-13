#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
request.get(args[0], { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const dict = {};
  for (const task of body) {
    if (task.completed) {
      if (dict[task.userId]) {
        dict[task.userId] += 1;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
});
