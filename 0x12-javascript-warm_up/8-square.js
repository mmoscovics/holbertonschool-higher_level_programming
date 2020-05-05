#!/usr/bin/node
const number = process.argv[2];
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < number; y++) {
    console.log('X'.repeat(number));
  }
}
