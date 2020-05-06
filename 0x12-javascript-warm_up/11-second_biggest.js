#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  args.sort(function (a, b) { return a - b }).reverse();
  console.log(args[1]);
}
